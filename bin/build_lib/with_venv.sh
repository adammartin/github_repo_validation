#!/usr/bin/env bash

set_venv () {
    if [[ -z "${#JENKINS_URL}" ]]; then
        # Avoid long paths that lead to issues running pip in virtualenv
        # https://github.com/pypa/pip/issues/1773
        export VENV="$(mktemp -d "/tmp/venv.XXXXXXXX")"
    else
        export VENV="$PROJECT_DIR/venv/github_repo_validation"
    fi
}

with_venv () {
    . "$VENV/bin/activate"
}

if [[ ! -z "${#VENV}" ]]; then
    set_venv
fi
