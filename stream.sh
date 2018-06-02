#! bin/bash

cd /usr/src/mjpg-streamer/mjpg-streamer-experimental

export LD_LIBRARY_PATH=.
./mjpg_streamer -o "output_http.so -w ./www" -i "input_raspicam.so -x 1024 -y 768 -fps 25 -ex night"