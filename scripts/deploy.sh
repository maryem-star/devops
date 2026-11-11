#!/bin/sh
# Faux deploiement pour le TP
set -e
python -m unittest
echo "Deploiement de $(git describe --tags --always) termine"
