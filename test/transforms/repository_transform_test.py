from github_repo_validation.transforms import repository_transform
from github_repo_validation import repositories
from unittest import mock


class Config:
    REPO_PROPERTIES = ['attrib_1', 'attrib_2', 'url']


CONFIG = Config()
RECORD_1_ROOT_URL = 'WHERE'
RECORD_2_ROOT_URL = 'HOW'
RECORD_1_README = 'RECORD_1_README'
RECORD_2_README = 'RECORD_2_README'
BASE_RECORD_1 = { 'attrib_1': 'ONE', 'attrib_2': 'TWO', 'url': RECORD_1_ROOT_URL }
BASE_RECORD_2 = { 'attrib_1': 'THREE', 'attrib_2': 'FOUR', 'url': RECORD_2_ROOT_URL }
USELESS_ATTRIBS = { 'junk_1': 'POO', 'junk_2': 'BLARG' }
RECORD_1 = { **BASE_RECORD_1, **USELESS_ATTRIBS }
RECORD_2 = { **USELESS_ATTRIBS, **BASE_RECORD_2 }
REPOS = [ RECORD_1, RECORD_2 ]
EXPECTED_RECORD_1 = { **BASE_RECORD_1, 'readme': RECORD_1_README }
EXPECTED_RECORD_2 = { **BASE_RECORD_2, 'readme': RECORD_2_README }
EXPECTED_REPOS = [ EXPECTED_RECORD_1, EXPECTED_RECORD_2 ]


def get_readme_md(*args, **kwargs):
    if args[0] == RECORD_1_ROOT_URL and args[1] == CONFIG:
        return RECORD_1_README
    elif args[0] == RECORD_2_ROOT_URL and args[1] == CONFIG:
        return RECORD_2_README
    return None


@mock.patch('github_repo_validation.repositories.readme_md', side_effect=get_readme_md)
def test_will_only_return_attributes_we_want(readme_md_mock):
    assert repository_transform.transform_repos(REPOS, CONFIG) == EXPECTED_REPOS


@mock.patch('github_repo_validation.repositories.readme_md', side_effect=get_readme_md)
def test_will_handle_non_existant_attributes(readme_md_mock):
    bad_record = { 'url': 'blah', **USELESS_ATTRIBS }
    repos = [ RECORD_1, bad_record ]
    empty_result = { 'attrib_1': None, 'attrib_2': None, 'url': 'blah', 'readme': None }
    expected_repos = [ EXPECTED_RECORD_1, empty_result ]
    assert repository_transform.transform_repos(repos, CONFIG) == expected_repos


@mock.patch('github_repo_validation.repositories.readme_md', side_effect=get_readme_md)
def test_will_retrieve_readme(readme_md_mock):
    assert repository_transform.transform_repos(REPOS, CONFIG) == EXPECTED_REPOS
