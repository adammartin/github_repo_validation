import datetime
from github_repo_validation import repositories


def transform_repos(repos, config):
    return [_transform_repo(repo, config) for repo in repos]


def _transform_repo(repo, config):
    repository = {key: repo.get(key) for key in config.REPO_PROPERTIES}
    repository['readme'] = repositories.readme_md(repo.get('url'), config)
    repository['date'] = datetime.datetime.now().strftime("%Y-%m-%d")
    return repository
