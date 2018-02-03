#!/bin/bash

docker build . -t registry.heroku.com/twelve-factors/web
docker login --username=wisner.oliveira@gmail.com --password=$(echo $HEROKU_TOKEN) registry.heroku.com
docker push registry.heroku.com./twelve-factors/web