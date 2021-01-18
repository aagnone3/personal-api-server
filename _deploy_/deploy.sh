#!/usr/bin/env bash
set -eou pipefail

host=$1
directory=$2

declare -a deploy_src=(
    passenger_wsgi.py
    robots.txt
    tmp
    ../app
    ../requirements.txt
)
rsync --delete -azru ${deploy_src[@]} ${host}:${directory}/

ssh ${host} <<EOF
    source \$( find virtualenv -name activate | grep ${directory} | head -n1 )
    cd ${directory}
    pip install -r requirements.txt
    touch tmp/restart.txt
EOF
