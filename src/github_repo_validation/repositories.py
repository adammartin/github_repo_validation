import json
import requests

_ALL_REPOS = '/orgs/hisc/repos?access_token='


def repository_list(config):
    url = config.SOURCE_ROOT_URL + _ALL_REPOS + config.API_TOKEN
    return _get_all_paged(url, config)


def _get_all_paged(url, config):
    response = _get_response(url, config)
    all_data = json.loads(response.text)
    while _next(response.links):
        response = _get_response(_next(response.links), config)
        all_data = all_data + json.loads(response.text)
    return all_data


def _get_response(url, config):
    return requests.get(url, headers=config.SOURCE_HEADER)


def _next(links):
    if 'next' in links:
        return links['next']['url']
    return None
