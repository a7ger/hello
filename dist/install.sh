#!/usr/bin/env bash

if [ -d /usr/share/hello ]; then
    echo 'a program called hello already exists'
    exit
fi

cp hello /usr/bin/

mkdir /usr/share/hello
cp icon.png /usr/share/hello

cp hello.desktop /usr/share/applications/
