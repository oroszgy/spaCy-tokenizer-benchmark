#!/usr/bin/env bash

wget https://github.com/UniversalDependencies/UD_English/archive/r1.4.zip
unzip r1.4.zip
rm -rf r1.4.zip

mkdir corpus
python transformer.py
