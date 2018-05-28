from github_repo_validation.transforms import repository_transform
from unittest import mock


class Config:
    REPO_PROPERTIES = ['ATTRIB_1', 'ATTRIB_2', 'URL']


CONFIG = Config()
EXPECTED_RECORD_1 = { 'ATTRIB_1': 'ONE', 'ATTRIB_2': 'TWO', 'URL': 'WHERE' }
EXPECTED_RECORD_2 = { 'ATTRIB_1': 'ONE', 'ATTRIB_2': 'TWO', 'URL': 'HOW' }
USELESS_ATTRIBS = { 'JUNK_1': 'POO', 'JUNK_2': 'BLARG' }
RECORD_1 = { **EXPECTED_RECORD_1, **USELESS_ATTRIBS }
RECORD_2 = { **USELESS_ATTRIBS, **EXPECTED_RECORD_2 }
REPOS = [ RECORD_1, RECORD_2 ]
EXPECTED_REPOS = [ EXPECTED_RECORD_1, EXPECTED_RECORD_2 ]


def test_will_only_return_attributes_we_want():
    assert repository_transform.transform_repos(REPOS, CONFIG) == EXPECTED_REPOS


def test_will_handle_non_existant_attributes():
    repos = [ RECORD_1, USELESS_ATTRIBS ]
    empty_result = { 'ATTRIB_1': None, 'ATTRIB_2': None, 'URL': None }
    expected_repos = [ EXPECTED_RECORD_1, empty_result ]
    assert repository_transform.transform_repos(repos, CONFIG) == expected_repos
