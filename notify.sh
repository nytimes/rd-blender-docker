#!/bin/bash
curl -X POST -H 'Content-type: application/json' --data '{"text":"Blender Docker images deployed to Docker Hub :party:", "icon_emoji": ":blender-3d:"}' ${WEBHOOK_URL}