import string_utils


_WEIGHT = 'compliance_weight'


def rules():
    return [readme_rule, topics_rule, name_rule, organizations_rule]


# pylint: disable=unused-argument
# Point of these methods is to match a signature so that they can be iterated
# over.  As such there can be unused arguments
def readme_rule(repo, config):
    size = repo.get('readme', {}).get('size', 0)
    repo[_WEIGHT] = _new_repo_weight(repo, _readme_weight(size))
    if 'readme' in repo:
        repo.pop('readme')
    return repo


def topics_rule(repo, config):
    topics = repo.get('topics', [])
    weight = _topic_weight(len(topics))
    repo[_WEIGHT] = _new_repo_weight(repo, weight)
    return repo


def organizations_rule(repo, config):
    weight = 0
    topics = repo.get('topics', [])
    if _contains_any_organization(topics, config.ORGANIZATIONS):
        weight = 1
    repo[_WEIGHT] = _new_repo_weight(repo, weight)
    return repo


def name_rule(repo, config):
    name = repo['full_name'].replace('HISC/', '')
    repo['name_compliance'] = string_utils.is_snake_case(name)
    return repo


def _topic_weight(count):
    if count >= 2:
        return 1
    return count/2


def _readme_weight(size):
    if size >= 1500:
        return 1
    return size/1500


def _contains_any_organization(topics, organizations):
    if [topic for topic in topics for org in organizations if topic in org]:
        return True
    return False


def _new_repo_weight(repo, weight):
    return repo.get(_WEIGHT, 1) * weight
