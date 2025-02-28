#! /usr/bin/env bash
# run this script to start the server

# write messages to stderr
err () {
    echo "ERROR: $1" > /dev/stderr
}

filename="$(basename $0)"
if [[ "$0" != "./$filename" ]]; then
    err "run script from it's directory"
    exit 1
fi

if [[ !-d ./.venv ]]; then
    err "run setup script first"
    exit 1
fi

. .venv/bin/activate
if [[ $? -ne 0 ]]; then
    err "failed to activate venv"
fi

echo "STARTING DAEMON..."
nohup $(python3 daemon.py &> daemon.out) &

echo "STARTING SERVER..."
nohup $(python3 server.py &> server.out) &
