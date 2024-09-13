# LincARI
ROS noetic packages for the ARI robot in L-CAS.

**These packages are to be run on an external PC to the robot and connected either via ETH or the robot's wifi.**

## Setup

1. Install the following packages:
  - `pip install tmule pymongo`
  - `sudo apt-get install mongodb mongodb-dev python3-pymongo`

2. [Create a ROS workspace](http://wiki.ros.org/catkin/Tutorials/create_a_workspace) in `~/workspaces/ARI_ws`.

3. Inside `ARI_ws/src`
   a. clone mongodb_store: `git clone -b noetic_devel https://github.com/strands-project/mongodb_store.git`
   b. clone this repo: `git clone https://github.com/LCAS/LincARI.git`

4. Install dependencies: `rosdep update && rosdep install --from-paths . -i -y`
5. Build the workspace: `catkin build`

## Running

```
tmule -c tmule -c src/LincARI/lincari_bringup/config/rob_ARI.yaml launch launch
```

## Configuration data collection
By default the mongo database will be created inside `ARI_ws/db/ARI`. Each topic is stored in its own collection inside the `ari_message_store` database.

You can edit the topics that are logged by editing the file `LincARI/lincari_logging/config/topics_to_log_list.txt`.
