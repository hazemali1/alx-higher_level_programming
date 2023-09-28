#!/bin/bash
#OPTIONS
curl -sX OPTIONS $1 | grep 'Allow' | cut -c 8-
