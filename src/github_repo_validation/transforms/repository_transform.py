from github_repo_validation import repositories


def transform_repos(repositories, config):
    return [_transform_repo(repo, config) for repo in repositories]


def _transform_repo(repo, config):
    repository = {key: repo.get(key) for key in config.REPO_PROPERTIES}
    repository['readme'] = repositories.readme_md(_readme_url(repo), config)
    return repository


def _readme_url(repo):
    return repo.get('url') + '/readme'
