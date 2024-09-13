#!/bin/bash

export LINCARI_TOPICS_LOG=$(cat $(rospack find lincari_logging)/config/topics_to_log_list.txt)

rosrun mongodb_log mongodb_log.py --mongodb-host=localhost --mongodb-port=62345 --mongodb-name=ari_message_store $LINCARI_TOPICS_LOG #> ~/.ros/mongodb_log.log >>&1
