from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
import os

app = Flask(__name__)
api = Api(app)


def updateREADME(category, title, link):
    readme = open("/Users/bellroot/Desktop/tipgetter/README.md", 'r')

    list = readme.readlines()

    index = list.index("## {:}\n".format(category))

    for i in range(index, len(list)):
        if list[i] == "\n":
            list[i] = "- [{:}]({:})".format(title, link)
            break

    readme.close()

    with open('/Users/bellroot/Desktop/tipgetter/README.md', 'w') as file:
        file.writelines(list)


class PushCommit(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('title', type=str)
            parser.add_argument('link', type=str)
            parser.add_argument('category', type=str)
            args = parser.parse_args()

            _title = args['title']
            _link = args['link']
            _category = args['category']

            # os.system("git pull origin master")

            updateREADME(_category, _title, _link)

            # os.system("git add .")
            # os.system('git commit -m "{:}: {:}"'.format(_category, _title))
            # os.symlink('git push origin master')

            return {'Title': _title, 'Link': _link, 'Category': _category}
        except Exception as e:
            return {'error': str(e)}


api.add_resource(PushCommit, '/push')

if __name__ == '__main__':
    app.run(debug=True)
