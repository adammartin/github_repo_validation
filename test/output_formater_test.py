from github_repo_validation.output_formater import format_output
import json
from unittest import mock


HEADER_1 = 'blarg'
HEADER_2 = 'foo'
REPO_1 = { HEADER_1: 'blah', HEADER_2: 'bar' }
REPO_2 = { HEADER_1: 'poo', HEADER_2: 'baz' }
REPOS = [REPO_1, REPO_2]
CSV = 'csv'
JSONL = 'jsonl'
FILE_NAME = 'derp'


@mock.patch("builtins.open", new_callable=mock.mock_open)
def test_will_print_to_csv_file(my_open):
    format_output(REPOS, CSV, FILE_NAME)
    FULL_FILE_NAME = FILE_NAME + '.' + CSV
    my_open.assert_called_once_with(FULL_FILE_NAME, 'w')


@mock.patch("builtins.open", new_callable=mock.mock_open)
def test_will_will_write_csv_headers(my_open):
    format_output(REPOS, CSV, FILE_NAME)
    output = my_open()
    headers = HEADER_1 + ',' + HEADER_2 + '\r\n'
    output.write.assert_any_call(headers)


@mock.patch("builtins.open", new_callable=mock.mock_open)
def test_will_will_write_csv_content(my_open):
    format_output(REPOS, CSV, FILE_NAME)
    output = my_open()
    line_1 = REPO_1[HEADER_1] + ',' + REPO_1[HEADER_2] + '\r\n'
    line_2 = REPO_2[HEADER_1] + ',' + REPO_2[HEADER_2] + '\r\n'
    output.write.assert_any_call(line_1)
    output.write.assert_called_with(line_2)


@mock.patch("builtins.open", new_callable=mock.mock_open)
def test_will_print_to_jsonl_file(my_open):
    format_output(REPOS, JSONL, FILE_NAME)
    FULL_FILE_NAME = FILE_NAME + '.' + JSONL
    my_open.assert_called_once_with(FULL_FILE_NAME, 'w')


@mock.patch("builtins.open", new_callable=mock.mock_open)
def test_will_will_write_jsonl_content(my_open):
    format_output(REPOS, JSONL, FILE_NAME)
    output = my_open()
    line_1 = json.dumps(REPO_1) + '\n'
    line_2 = json.dumps(REPO_2) + '\n'
    output.writelines.assert_any_call(line_1)
    output.writelines.assert_called_with(line_2)
