from github_repo_validation.filters import rules_factory
from unittest import mock


EXPECTED_RULES = [rules_factory.readme_rule, rules_factory.topics_rule]


def test_will_return_list_of_rules():
    assert rules_factory.rules() == EXPECTED_RULES


WEIGHT = 'compliance_weight'
MIN_DESIRED_SIZE = 1500 # This is arbitrary
GOOD_README = { 'size': MIN_DESIRED_SIZE }
OK_README = { 'size': 800 }
BAD_README = { 'size': 50 }
REALLY_GOOD_README = { 'size': 20000 }
NO_README = { 'documentation_url': 'blah', 'message': 'Not Found' }
MINIMUM_TOPICS = 2
REALLY_GOOD_TOPICS = [ 'one', 'two', 'three', 'four' ]
GOOD_TOPICS = [ 'one', 'two' ]
OK_TOPICS = [ 'one' ]
BAD_TOPICS = []


########## README TEST ##########

def sample_repo(readme=GOOD_README, topics=GOOD_TOPICS):
    return { 'readme': readme, 'topics': topics }


def test_will_weight_a_good_readme_at_1():
    repo = sample_repo(readme=GOOD_README)
    assert rules_factory.readme_rule(repo)[WEIGHT] == 1


def test_will_weight_an_ok_readme_as_percantage_of_1500_bytes():
    repo = sample_repo(readme=OK_README)
    expected_weight = OK_README['size']/MIN_DESIRED_SIZE
    assert rules_factory.readme_rule(repo)[WEIGHT] == expected_weight


def test_will_account_for_existing_weight_with_readme():
    repo = sample_repo(readme=OK_README)
    repo[WEIGHT] = 0.5
    expected_weight = repo[WEIGHT] * OK_README['size']/MIN_DESIRED_SIZE
    assert rules_factory.readme_rule(repo)[WEIGHT] == expected_weight


def test_will_weight_a_bad_readme_as_percantage_of_1500_bytes():
    repo = sample_repo(readme=BAD_README)
    expected_weight = BAD_README['size']/MIN_DESIRED_SIZE
    assert rules_factory.readme_rule(repo)[WEIGHT] == expected_weight


def test_will_weight_no_readme_as_0():
    repo = sample_repo(readme=NO_README)
    assert rules_factory.readme_rule(repo)[WEIGHT] == 0


def test_will_weight_0_if_missing_readme():
    assert rules_factory.readme_rule({})[WEIGHT] == 0


def test_will_remove_readme_attribute_for_space():
    repo = sample_repo()
    assert ('readme' in rules_factory.readme_rule(repo)) == False


def test_will_weight_a_really_good_readme_at_1():
    repo = sample_repo(readme=REALLY_GOOD_README)
    assert rules_factory.readme_rule(repo)[WEIGHT] == 1


########## TOPICS TEST ##########
# In the future we should have a list of acceptable organizations
# that should exist as topics until then good is defined as having 2

def test_will_weight_good_topics_at_1():
    repo = sample_repo(topics=GOOD_TOPICS)
    assert rules_factory.topics_rule(repo)[WEIGHT] == 1


def test_will_weight_really_good_topics_at_1():
    repo = sample_repo(topics=REALLY_GOOD_TOPICS)
    assert rules_factory.topics_rule(repo)[WEIGHT] == 1


def test_will_weight_ok_topcis_as_a_percentage_of_2_topics():
    repo = sample_repo(topics=OK_TOPICS)
    expected_weight = len(OK_TOPICS)/MINIMUM_TOPICS
    assert rules_factory.topics_rule(repo)[WEIGHT] == expected_weight


def test_will_weight_no_topics_as_0():
    repo = sample_repo(topics=BAD_TOPICS)
    assert rules_factory.topics_rule(repo)[WEIGHT] == 0


def test_will_weight_repo_missing_topics_as_0():
    repo = {}
    assert rules_factory.topics_rule(repo)[WEIGHT] == 0


def test_will_account_forexisting_weight_with_topics():
    repo = sample_repo(topics=OK_TOPICS)
    repo[WEIGHT] = 0.5
    expected_weight = repo[WEIGHT] * len(OK_TOPICS)/MINIMUM_TOPICS
    assert rules_factory.topics_rule(repo)[WEIGHT] == expected_weight
