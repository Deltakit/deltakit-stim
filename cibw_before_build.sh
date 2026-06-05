#!/bin/bash

if [ "$(uname)" == "Linux" ]
then
    yum update -y
    yum install -y openssh-clients
    mkdir -p ~/.ssh
    chmod 700 ~/.ssh
    ssh-keyscan github.com >> ~/.ssh/known_hosts
    yum install gcc-toolset-11 -y
elif [ "$(uname)" == "Darwin" ]
then
    brew install llvm@16
else
    echo "Platform not supported"
    exit 1
fi

echo "CIBW before build sucessfully completed!"