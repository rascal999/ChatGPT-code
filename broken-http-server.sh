#!/usr/bin/env bash

# Listen for incoming connections on port 8080.
nc -l 8080 > /dev/null

# Read the request data from the network.
REQUEST=$(cat)

# Write a simple response to the client.
echo -e "HTTP/1.1 200 OK\n\nHello, World!"
