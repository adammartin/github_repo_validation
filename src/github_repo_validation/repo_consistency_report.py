import csv
import json
import click
import config
from validation_checks import repositories_in_violation


@click.command()
@click.option('--print_format', type=click.Choice(['jsonl', 'csv']))
def repo_consistency_report(print_format='jsonl'):
    if print_format == 'jsonl':
        _print_jsonl()
    _print_csv()


def _print_jsonl():
    with open('repos.jsonl', 'w') as output:
        for entry in repositories_in_violation(config):
            output.writelines(json.dumps(entry)+'\n')


def _print_csv():
    with open('repos.csv', 'w') as output:
        repos = repositories_in_violation(config)
        fieldnames = repos[0].keys()
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(repos)


if __name__ == "__main__":
    repo_consistency_report()
