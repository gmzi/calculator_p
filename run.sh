#!/bin/bash

python3 -m http.server -d ./public/ &

node server/data.js &

# wait