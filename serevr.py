from flask import Flask
from flask_restful import Api, Resource, reqparse
from git_management_api.views.repo import RepoViews
import logging
logger = logging.getLogger(__name__)
app = Flask(__name__)
api = Api(app)

api.add_resource(RepoViews, '/repo/<string:post_url>')
if __name__ == '__main__':
    app.run(debug=True)
