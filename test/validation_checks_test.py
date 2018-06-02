from github_repo_validation.validation_checks import repositories_in_violation
from github_repo_validation.repositories import repository_list
from github_repo_validation.filters import filter_rules
from github_repo_validation.transforms import repository_transform
from unittest import mock


BAD_REPOS = 'BAD_REPO'
TRANSFORM_REPOS = 'TRANSFORM_REPOS'
ALL_REPOS = 'ALL_REPOS'
CONFIG = 'some_config'


def transform_mock(*args, **kwargs):
    if args[0] == ALL_REPOS and args[1] == CONFIG:
        return TRANSFORM_REPOS
    return None


def filter_mock(*args, **kwargs):
    if args[0] == TRANSFORM_REPOS and args[1] == CONFIG:
        return BAD_REPOS
    return None


@mock.patch('github_repo_validation.filters.filter_rules.FilterRules', auto_spec=True)
@mock.patch('github_repo_validation.repositories.repository_list', return_value=ALL_REPOS)
@mock.patch('github_repo_validation.transforms.repository_transform.transform_repos', side_effect=transform_mock)
def test_will_only_return_the_repositories_in_violation(transforms_mock, repository_list_function_mock, filters_rules_mock):
    filters_rules_mock.return_value.filter.side_effect = filter_mock
    assert repositories_in_violation(CONFIG) == BAD_REPOS
