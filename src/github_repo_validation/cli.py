import click
from github_repo_validation import config
from github_repo_validation.validation_checks import repositories_in_violation
from github_repo_validation.output_formater import format_output


@click.command()
@click.option('--print_format', type=click.Choice(['jsonl', 'csv']))
def repo_consistency_report(print_format):
    format_output(repositories_in_violation(config), print_format, 'repos')

if __name__ == "__main__":
    repo_consistency_report('csv')
