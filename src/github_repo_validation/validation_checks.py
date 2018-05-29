from github_repo_validation import repositories
from github_repo_validation.filters import filter_rules
from github_repo_validation.transforms import repository_transform


def repositories_in_violation(config):
    my_rules = filter_rules.FilterRules()
    all_repos = repositories.repository_list(config)
    transformed_repos = repository_transform.transform_repos(all_repos, config)
    return my_rules.filter(transformed_repos)
