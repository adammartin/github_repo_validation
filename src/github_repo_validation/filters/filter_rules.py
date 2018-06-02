from github_repo_validation.filters import rules_factory


# pylint: disable=too-few-public-methods
class FilterRules:
    def __init__(self):
        self.rules = rules_factory.rules()

    def filter(self, repository_list, config):
        return [self._apply_filters(repo, config) for repo in repository_list]

    def _apply_filters(self, repo, config):
        repository = dict(repo)
        for rule in self.rules:
            repository = rule(repository, config)
        return repository
