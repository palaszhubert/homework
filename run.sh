#!/bin/bash
#Info: Start or restart docker-compose app in directory. 
docker-compose restart || echo 'APP_PORT='${1:-5000}>.env && docker-compose up




