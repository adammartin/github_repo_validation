# GitHub Repo Validation

Python modules to check if repositories in alignment with desired standards

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
