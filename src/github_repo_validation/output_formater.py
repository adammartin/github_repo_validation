import csv
import json


def format_output(repositories, print_format, file_name):
    with open(_full_file_name(file_name, print_format), 'a') as output:
        if print_format == 'csv':
            _write_csv(output, repositories)
        elif print_format == 'jsonl':
            _write_jsonl(output, repositories)


def _write_csv(output, repositories):
    fieldnames = repositories[0].keys()
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(repositories)


def _write_jsonl(output, repositories):
    for entry in repositories:
        output.writelines(json.dumps(entry)+'\n')


def _full_file_name(file_name, print_format):
    return file_name + '.' + print_format
