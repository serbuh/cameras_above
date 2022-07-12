#!/bin/bash

if [ "$1" = "-h" ]; then
	echo "$0 <rtsp_url> <duration_sec> <folder> <file>"
	echo 'Eg: ./record_segments.sh rtsp://admin:UOXBGL@192.168.0.233:554/H.264" 300 "Videos" "UOXBGL"'
	exit
fi

ffmpeg -i $1 -vcodec copy -acodec copy -map 0 -f segment -segment_time $2 -segment_format mp4 "$3/$4-%03d.mp4"

