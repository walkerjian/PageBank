#!/bin/bash
# Run the PageBank container with live source code and API key injection

docker run --rm -it \
  --env-file .env \
  -v "$(pwd)":/app \
  pagebank
