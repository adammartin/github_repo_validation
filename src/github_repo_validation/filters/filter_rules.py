from github_repo_validation.filters import rules_factory


# pylint: disable=too-few-public-methods, unused-variable
class FilterRules:
    def __init__(self, config):
        self.config = config
        self.rules = rules_factory.rules()

    def filter(self, repository_list):
        return [self._apply_filters(repo) for repo in repository_list]

    def _apply_filters(self, repo):
        repository = dict(repo)
        for rule in self.rules:
            repository = rule(repository)
        return repository
