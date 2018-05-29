from github_repo_validation.filters import rules_factory
from unittest import mock


EXPECTED_RULES = []


def test_will_return_list_of_rules():
    assert rules_factory.rules() == EXPECTED_RULES
