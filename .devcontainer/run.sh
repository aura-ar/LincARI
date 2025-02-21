#!/bin/bash


add_source_bashrc () {
    if ! grep -q "source $1" ~/.bashrc; then 
        echo "source $1" >> ~/.bashrc
    fi 
}

set -e

source /opt/pal/gallium/setup.bash
sudo apt update
sudo rosdep init
sudo rosdep update 



add_source_bashrc "/opt/pal/gallium/setup.bash"