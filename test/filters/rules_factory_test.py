from github_repo_validation.filters import rules_factory
from unittest import mock


EXPECTED_RULES = [rules_factory.readme_rule,
                  rules_factory.topics_rule,
                  rules_factory.name_rule,
                  rules_factory.organizations_rule]


def test_will_return_list_of_rules():
    assert rules_factory.rules() == EXPECTED_RULES


ORG_1 = 'two'
ORG_2 = 'three'


class Config:
    ORGANIZATIONS = [ORG_1, ORG_2]


CONFIG = Config()
WEIGHT = 'compliance_weight'
VALID_NAME = 'name_compliance'
MIN_DESIRED_SIZE = 1500 # This is arbitrary
GOOD_README = { 'size': MIN_DESIRED_SIZE }
OK_README = { 'size': 800 }
BAD_README = { 'size': 50 }
REALLY_GOOD_README = { 'size': 20000 }
NO_README = { 'documentation_url': 'blah', 'message': 'Not Found' }
MINIMUM_TOPICS = 2
REALLY_GOOD_TOPICS = [ 'one', ORG_1, ORG_2, 'four' ]
GOOD_TOPICS = [ 'one', ORG_1 ]
OK_TOPICS = [ 'one' ]
BAD_TOPICS = []
SNAKE_NAME = 'good_name'
CAMEL_NAME = 'BadName'
MIXED_NAME = 'MC.hammer_time'


def sample_repo(readme=GOOD_README, topics=GOOD_TOPICS, name='SNAKE_NAME'):
    return { 'readme': readme, 'topics': topics, 'full_name': 'HISC/'+name }


class TestReadme:

    def test_will_weight_a_good_readme_at_1(self):
        repo = sample_repo(readme=GOOD_README)
        assert rules_factory.readme_rule(repo, CONFIG)[WEIGHT] == 1

    def test_will_weight_an_ok_readme_as_percantage_of_1500_bytes(self):
        repo = sample_repo(readme=OK_README)
        expected_weight = OK_README['size']/MIN_DESIRED_SIZE
        assert rules_factory.readme_rule(repo, CONFIG)[WEIGHT] == expected_weight

    def test_will_account_for_existing_weight_with_readme(self):
        repo = sample_repo(readme=OK_README)
        repo[WEIGHT] = 0.5
        expected_weight = repo[WEIGHT] * OK_README['size']/MIN_DESIRED_SIZE
        assert rules_factory.readme_rule(repo, CONFIG)[WEIGHT] == expected_weight

    def test_will_weight_a_bad_readme_as_percantage_of_1500_bytes(self):
        repo = sample_repo(readme=BAD_README)
        expected_weight = BAD_README['size']/MIN_DESIRED_SIZE
        assert rules_factory.readme_rule(repo, CONFIG)[WEIGHT] == expected_weight

    def test_will_weight_no_readme_as_0(self):
        repo = sample_repo(readme=NO_README)
        assert rules_factory.readme_rule(repo, CONFIG)[WEIGHT] == 0

    def test_will_weight_0_if_missing_readme(self):
        assert rules_factory.readme_rule({}, CONFIG)[WEIGHT] == 0

    def test_will_remove_readme_attribute_for_space(self):
        repo = sample_repo()
        assert ('readme' in rules_factory.readme_rule(repo, CONFIG)) == False

    def test_will_weight_a_really_good_readme_at_1(self):
        repo = sample_repo(readme=REALLY_GOOD_README)
        assert rules_factory.readme_rule(repo, CONFIG)[WEIGHT] == 1


class TestTopics:

    def test_will_weight_good_topics_at_1(self):
        repo = sample_repo(topics=GOOD_TOPICS)
        assert rules_factory.topics_rule(repo, CONFIG)[WEIGHT] == 1

    def test_will_weight_really_good_topics_at_1(self):
        repo = sample_repo(topics=REALLY_GOOD_TOPICS)
        assert rules_factory.topics_rule(repo, CONFIG)[WEIGHT] == 1

    def test_will_weight_ok_topcis_as_a_percentage_of_2_topics(self):
        repo = sample_repo(topics=OK_TOPICS)
        expected_weight = len(OK_TOPICS)/MINIMUM_TOPICS
        assert rules_factory.topics_rule(repo, CONFIG)[WEIGHT] == expected_weight

    def test_will_weight_no_topics_as_0(self):
        repo = sample_repo(topics=BAD_TOPICS)
        assert rules_factory.topics_rule(repo, CONFIG)[WEIGHT] == 0

    def test_will_weight_repo_missing_topics_as_0(self):
        repo = {}
        assert rules_factory.topics_rule(repo, CONFIG)[WEIGHT] == 0

    def test_will_account_forexisting_weight_with_topics(self):
        repo = sample_repo(topics=OK_TOPICS)
        repo[WEIGHT] = 0.5
        expected_weight = repo[WEIGHT] * len(OK_TOPICS)/MINIMUM_TOPICS
        assert rules_factory.topics_rule(repo, CONFIG)[WEIGHT] == expected_weight


class TestOrganization:

    def test_will_weight_existance_of_organization_at_1(self):
        repo = sample_repo(topics=GOOD_TOPICS)
        assert rules_factory.organizations_rule(repo, CONFIG)[WEIGHT] == 1

    def test_will_weight_no_organization_at_0(self):
        repo = sample_repo(topics=OK_TOPICS)
        assert rules_factory.organizations_rule(repo, CONFIG)[WEIGHT] == 0

    def test_will_weight_no_topics_for_organizations_as_0(self):
        repo = sample_repo(topics=BAD_TOPICS)
        assert rules_factory.organizations_rule(repo, CONFIG)[WEIGHT] == 0

    def test_will_weight_repo_missing_topics_for_organizations_as_0(self):
        repo = {}
        assert rules_factory.organizations_rule(repo, CONFIG)[WEIGHT] == 0

    def test_will_account_for_existing_weight_with_organizations(self):
        repo = sample_repo(topics=GOOD_TOPICS)
        repo[WEIGHT] = 0.5
        expected_weight = 0.5
        assert rules_factory.readme_rule(repo, CONFIG)[WEIGHT] == expected_weight


class TestName:

    def test_will_pass_snake_case_name(self):
        repo = sample_repo(name=SNAKE_NAME)
        assert rules_factory.name_rule(repo, CONFIG)[VALID_NAME] == True

    def test_will_fail_camel_case_name(self):
        repo = sample_repo(name=CAMEL_NAME)
        assert rules_factory.name_rule(repo, CONFIG)[VALID_NAME] == False

    def test_will_fail_mixed_case_name(self):
        repo = sample_repo(name=MIXED_NAME)
        assert rules_factory.name_rule(repo, CONFIG)[VALID_NAME] == False
