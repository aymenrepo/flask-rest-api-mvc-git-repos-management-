from git import Repo

class RepoController:

    def clone_repo(self, **kwargs):

        try:

            directory = kwargs.get('directory')
            repo_url = kwargs.get('repo_url')
            Repo.clone_from(url=repo_url, to_path=directory)
            return dict(reposotroy=repo_url, to_path=directory)

        except Exception as e:

            return dict(status="error", error=e)