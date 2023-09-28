#!/bin/bash
# size of the body
curl -s -I $1 | grep Content-Length | cut -c 17-
