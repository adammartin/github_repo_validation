def transform_repos(repositories, config):
    return [_transform_repo(repo, config) for repo in repositories]


def _transform_repo(repo, config):
    return {key: repo.get(key) for key in config.REPO_PROPERTIES}
