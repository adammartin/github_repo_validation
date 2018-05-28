import json
import click
import config
from validation_checks import repositories_in_violation


@click.command()
def repo_consistency_report():
    # SHOULD: change config to environment variables
    with open('repos.json', 'w') as output:
        output.write(json.dumps(repositories_in_violation(config)))

if __name__ == "__main__":
    repo_consistency_report()
