#!/bin/bash
#OPTIONS
curl -sIX OPTIONS $1 | grep 'Allow' | cut -c 8-
