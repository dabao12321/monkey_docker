#!/bin/bash

# run by "./containerize <dir_path> <container_img>"

echo "starting ..."
python filespawn.py $1
cd $1
docker build -t $2 .
echo "running"
docker run -dit $2

# TODO: store container id to execute
# echo ${container_id}
# docker exec -it container_id /bin/bash

echo "done"
