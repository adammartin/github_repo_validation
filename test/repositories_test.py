from github_repo_validation.repositories import repository_list, readme_md
from unittest import mock
import requests, json, httpretty


class Config:
    API_TOKEN = 'blarg'
    SOURCE_ROOT_URL = 'https://URI'
    SOURCE_HEADER = {'foo': 'bar'}


CONFIG = Config()
BASE_URL = CONFIG.SOURCE_ROOT_URL + '/orgs/hisc/repos?access_token=' + CONFIG.API_TOKEN
REPO_URL = 'https://A_REPO_URL.com'
REPO_README_URL = REPO_URL + '/readme?access_token=' + CONFIG.API_TOKEN
NEXT_URL = 'https://nexturl.com'
RESPONSE_LIST_1 = ['stuff']
RESPONSE_LIST_2 = ['other_stuff']


def register_uri_call(url, response, links=''):
    httpretty.register_uri(httpretty.GET,
                           url,
                           body=json.dumps(response),
                           adding_headers={'Link': links})

@httpretty.activate
def test_repository_list_will_retrieve_repositories():
    register_uri_call(BASE_URL, RESPONSE_LIST_1)
    assert repository_list(CONFIG) == RESPONSE_LIST_1


@httpretty.activate
def test_repository_list_will_retrieve_paged_repositories():
    links = '<' + NEXT_URL + '>; rel="next"'
    register_uri_call(BASE_URL, RESPONSE_LIST_1, links)
    register_uri_call(NEXT_URL, RESPONSE_LIST_2)
    assert repository_list(CONFIG) == RESPONSE_LIST_1 + RESPONSE_LIST_2


@httpretty.activate
def test_readme_md_request_will_retrieve_readme():
    register_uri_call(REPO_README_URL, RESPONSE_LIST_1)
    assert readme_md(REPO_URL, CONFIG) == RESPONSE_LIST_1
