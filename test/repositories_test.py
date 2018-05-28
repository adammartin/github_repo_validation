from github_repo_validation.repositories import repository_list
from unittest import mock
import requests, json

class Config:
    API_TOKEN = 'blarg'
    SOURCE_ROOT_URL = 'root_url'
    SOURCE_HEADER = 'blah'

CONFIG = Config()
BASE_URL = CONFIG.SOURCE_ROOT_URL + '/orgs/hisc/repos?access_token=' + CONFIG.API_TOKEN
NEXT = 'next_url'
RESPONSE_LIST_1 = ['stuff']
RESPONSE_LIST_2 = ['other_stuff']
RESPONSE_JSON_1 = json.dumps(RESPONSE_LIST_1)
RESPONSE_JSON_2 = json.dumps(RESPONSE_LIST_2)

class Response:
    def __init__(self, text, next):
        self.links = {'next': {'url': next } }
        self.text = text

def mock_response(*args, **kwargs):
    if args[0] == BASE_URL and kwargs.get('headers'):
        return Response(RESPONSE_JSON_1, NEXT)
    elif args[0] == NEXT and kwargs.get('headers'):
        return Response(RESPONSE_JSON_2, None)
    return Response(None, None)

@mock.patch('requests.get', return_value = Response(RESPONSE_JSON_1, None))
def test_repository_list_will_retrieve_repositories(requests_mock):
    expected_url = CONFIG.SOURCE_ROOT_URL + '/orgs/hisc/repos?access_token=' + CONFIG.API_TOKEN
    assert repository_list(CONFIG) == RESPONSE_LIST_1

@mock.patch('requests.get', side_effect = mock_response)
def test_repository_list_will_retrieve_paged_repositories(requests_mock):
    expected_url = CONFIG.SOURCE_ROOT_URL + '/orgs/hisc/repos?access_token=' + CONFIG.API_TOKEN
    assert repository_list(CONFIG) == RESPONSE_LIST_1 + RESPONSE_LIST_2
