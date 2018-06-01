import click
import config
from validation_checks import repositories_in_violation
from output_formater import format_output


@click.command()
@click.option('--print_format', type=click.Choice(['jsonl', 'csv']))
def repo_consistency_report(print_format='jsonl'):
    format_output(repositories_in_violation(config), print_format, 'repos')

if __name__ == "__main__":
    repo_consistency_report()
