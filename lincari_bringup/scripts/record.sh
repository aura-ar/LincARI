#!/bin/bash

# List your topics (space-separated)
TOPICS="/tf /tf_static /look_at /pal_face/faces /robot_face /robot_face/.* /diagnostics_agg /humans/bodies/.* /map /robot_pose /humans/faces/.* /humans/persons/.*"

# Bag name with timestamp
BAG_NAME="Data_$(date +%Y%m%d_%H%M%S).bag"

echo "Recording rosbag: $BAG_NAME"
echo "Topics: $TOPICS"

rosbag record --lz4 -e -O "$BAG_NAME" $TOPICS


