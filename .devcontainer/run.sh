#!/bin/bash


add_source_bashrc () {
    if ! grep -q "source $1" ~/.bashrc; then 
        echo "source $1" >> ~/.bashrc
    fi 
}

set -e


curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -

source /opt/pal/gallium/setup.bash
sudo apt update
sudo apt upgrade
sudo rosdep init
sudo rosdep update 



add_source_bashrc "/opt/pal/gallium/setup.bash"