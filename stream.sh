#! bin/bash

cd /usr/src/mjpg-streamer/mjpg-streamer-experimental

export LD_LIBRARY_PATH=.
./mjpg_streamer -o "output_http.so -w ./www" -i "input_raspicam.so -x 800 -y 600 -fps 40 -ex night -rot 180"