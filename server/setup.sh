#! /usr/bin/env bash
# run this script once to set up the server

echo "SETTING UP SERVER..."

# INSTALL REQUIREMENTS

# update and upgrade
sudo apt update
sudo apt upgrade -y

# install tools
sudo apt install -y git curl neovim

# install programs
sudo apt install -y python3
