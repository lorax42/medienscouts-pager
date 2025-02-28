#! /usr/bin/env bash
# run this script once to set up the server

# write messages to stderr
err () {
    echo "ERROR: $1" > /dev/stderr
}

filename="$(basename $0)"
if [[ "$0" != "./$filename" ]]; then
    err "run script from it's directory"
    exit 1
fi

if [[ -d ./.venv ]]; then
    err "system already setup?"
    exit 1
fi

echo "SETTING UP SERVER..."

### INSTALL REQUIREMENTS ##

# update and upgrade
echo "updating system..."
sudo apt update
sudo apt upgrade -y

# install tools
echo "installing tools..."
sudo apt install -y git curl neovim

# setup python
echo "installing python..."
sudo apt install -y\
    python3\
    python3-pip

echo "setting up python environment..."
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
