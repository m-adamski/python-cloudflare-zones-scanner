#!/usr/bin/env bash

cd "$(dirname "$0")" || exit

if [ -d "../venv/Scripts" ] && [ -f "../venv/Scripts/activate" ]; then
    source ../venv/Scripts/activate &&
        python ../main "$@" &&
        deactivate
fi
