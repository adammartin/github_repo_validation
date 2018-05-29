from github_repo_validation.filters import filter_rules, rules_factory
from unittest import mock


COMPLIANCE = 'compliance_weight'


def fake_rule_1(repository):
    value = 1
    if repository['attrib_1'] < 1:
        value = 0.5
    repository[COMPLIANCE] = repository.get(COMPLIANCE, 1) * value
    return repository


def fake_rule_2(repository):
    value = 1
    if repository['attrib_2'] < 1:
        value = 0.25
    repository[COMPLIANCE] = repository.get(COMPLIANCE, 1) * value
    return repository

REPO_1 = { 'attrib_1': 0, 'attrib_2': 2 }
REPO_2 = { 'attrib_1': 2, 'attrib_2': 0 }
REPO_3 = { 'attrib_1': 0, 'attrib_2': 1 }
RULES = [ fake_rule_1, fake_rule_2 ]
EXPECTED_REPO_1 = { **REPO_1, COMPLIANCE: 0.5 }
EXPECTED_REPO_2 = { **REPO_2, COMPLIANCE: 0.25 }
EXPECTED_REPO_3 = { **REPO_3, COMPLIANCE: 0.125 }


@mock.patch('github_repo_validation.filters.rules_factory.rules', return_value = RULES)
def test_filter_rules_will_apply_rules_across_a_repo(mock_factory):
    filters = filter_rules.FilterRules()
    assert filters.filter([REPO_1]) == [EXPECTED_REPO_1]


@mock.patch('github_repo_validation.filters.rules_factory.rules', return_value = RULES)
def test_filter_rules_will_apply_rules_across_two_repos(mock_factory):
    filters = filter_rules.FilterRules()
    assert filters.filter([REPO_1, REPO_2]) == [EXPECTED_REPO_1, EXPECTED_REPO_2]
