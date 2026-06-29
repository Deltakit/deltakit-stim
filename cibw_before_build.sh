#!/bin/bash

# Setup SSH on Linux
if [ "$(uname)" == "Linux" ]
then
    yum update -y
    yum install -y openssh-clients
    mkdir -p ~/.ssh
    chmod 700 ~/.ssh
    # Copy mounted SSH and git config files from staging path
    # See https://github.com/webfactory/ssh-agent#using-multiple-deploy-keys-inside-docker-builds
    if [ -d /host-ssh ]; then
        cp -rf /host-ssh/* ~/.ssh/
        # Rewrite key paths from runner home to container home
        sed -i "s|/home/runner/.ssh|$HOME/.ssh|g" ~/.ssh/config
        chown -R root:root ~/.ssh
        chmod 700 ~/.ssh
        chmod 600 ~/.ssh/config
        # Fix permissions on all key files
        find ~/.ssh -type f ! -name "*.pub" ! -name "known_hosts" ! -name "config" -exec chmod 600 {} \;
    fi
    if [ -f /host-gitconfig ]; then
        cp -f /host-gitconfig ~/.gitconfig
    fi
    ssh-keyscan github.com >> ~/.ssh/known_hosts
    echo "SSH config successfully setup"
fi

# Other pre-build tasks
if [ "$(uname)" == "Linux" ]
then
    yum install gcc-toolset-11 -y
elif [ "$(uname)" == "Darwin" ]
then
    brew install llvm@16
else
    echo "Platform not supported"
    exit 1
fi

echo "CIBW before build sucessfully completed!"
