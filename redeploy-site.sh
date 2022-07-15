#!/bin/bash

#cd into project folder
cd /root/project-ssquad-sally

#ensure git repo inside VPS has latest changes from main branch on GitHub
git fetch && git reset origin/main --hard

docker compose -f docker-compose.prod.yml down

docker compose -f docker-compose.prod.yml up -d --build
