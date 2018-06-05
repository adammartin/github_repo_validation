# GitHub Repo Validation

Python modules to check if repositories in alignment with desired standards.

You can use it, once installed, by executing the following command:

```sh
github_repo_validation --print_format=[INSERT DESIRED FORMAT csv OR jsonl]
```

It will output a repo.XXXX file that contains the measurable data on the repositories in question.

Configuration is managed in the config.py file.  Organizations allows you to adjust the list of desired `organizations` to match the HISC enterprise list of accepted topics for organizations.  The `repo_properties` defines the constrained list of properties of a repository we wish to pull.

```
API_TOKEN = [INSERT_GITHUB_API_TOKEN_HERE]
SOURCE_ROOT_URL = 'https://api.github.com'
SOURCE_HEADER = {'Accept': 'application/vnd.github.mercy-preview+json'}
REPO_PROPERTIES = ['full_name', 'topics', 'url']
ORGANIZATIONS = ['digital-solutions',
                 'immersion-active',
                 'marketing',
                 'hisc',
                 'it-services',
                 'it-support',
                 'it',
                 'finance']
```

### Repository Meta Data

* Department/Organization: HIDS
* Project: N/A

## Development

### Setup

#### Prerequisites


Running tasks requires Bash version 4.3 or greater. Check your Bash version with

```sh
bash --version
```

If your version is below this, install a newer version of Bash, e.g.,

```sh
brew install bash
```

Python version 3.6 or greater is required with pip installed.

To install dependencies using pip execute the following command in development environment:

```sh
pip install -r requirements.txt
```

To install dependencies using pip in the production environment use the following command:

```sh
pip install -r requirements.prod.txt
```

To install the local directory for testing and execution purposes use the following command at the root of the project.

```sh
pip install -e .

```

#### Environment Variables

Before running any tasks, be sure to source the build environment variables file:

```sh
. build_variables.sh
```


#### Initialize venv

```sh
bin/init_venv.sh
```


### Tasks

To run all tasks, invoke

```sh
bin/analyze_and_test.sh
```

To invoke individual tasks, see below:

#### Static analysis

```sh
bin/analyze_python.sh
```

#### Run the unit tests

```sh
bin/run_unit_tests.sh
```
