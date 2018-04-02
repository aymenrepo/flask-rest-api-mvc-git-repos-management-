from flask_restful import reqparse, Resource
from flask.views import MethodView
from git_management_api.controller.repo import RepoController
import logging
logger = logging.getLogger(__name__)

class RepoViews(Resource):

    controller = RepoController

    def post(self, post_url=None):

        if post_url == '/clone':
            params = reqparse.RequestParser()
            params.add_argument('directory', type=str, required=True)
            params.add_argument('repo_url', type=str, required=True)
            params.add_argument()
            kwargs = params.parse_args()
            logger.info("kwargs={}".format(kwargs))
            return controller.clone_repo(**kwargs)



