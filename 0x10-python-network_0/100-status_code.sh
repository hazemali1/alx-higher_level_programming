#!/bin/bash
# status code
curl -sX HEAD -w "%{http_code}" $1
