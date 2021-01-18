#!/usr/bin/env bash
set -eou pipefail

host=$1
directory=$2

ssh ${host} <<EOF
\$( cat enter-api-env-commands )
which pip
EOF
# cd ${directory}
# pip install -r requirements.txt
# touch tmp/restart.txt
