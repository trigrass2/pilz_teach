# pilz_teach

pilz_teach is a PRBT6 teaching software module:
*Jogging* the manipulator and *defining* poses as you are used to in robotics controllers, but using native ROS functionality.

It can be used without additional hardware (keyboard-only-mode by default) but has easy interfaces to connect to any external device.

## Instructions

### Prerequisites

- Install ros-melodic-desktop from binaries, following the [official instructions](http://wiki.ros.org/melodic/Installation/Ubuntu)
- Install the pilz packages by executing `apt install ros-melodic-pilz-*` and `apt install ros-melodic-prbt-*`
- Follow the [instructions for building ROS2 dashing from source](https://index.ros.org/doc/ros2/Installation/Dashing/Linux-Development-Setup/), but don't build it yet

### Build Dashing and the Bridge

- Make sure that you didn't set any ros-related environment variables for ROS or ROS2 in your current bash and go to your ros2_dashing workspace
- Build ROS2 save the ros1_bridge by executing `colcon build --symlink-install --packages-skip ros1_bridge`
- Then source your melodic installation, your dashing installation (`source ~/ros2_dashing/install/local_setup.bash`) and every workspace which contains message definitions you want be mapped from ROS to ROS2 and vice versa
- Build the ros1_bridge by executing `colcon build --symlink-install --packages-select ros1_bridge --cmake-force-configure`

Congratulations - you can now run the bridge via `ros2 run ros1_bridge dynamic_bridge`. Be default, only msg and srv are mapped (and thus visible), which exist in both, ROS and ROS2. You can change that behaviour by running the bridge with on of the flags
- `--bridge-all-1to2-topics`
- `--bridge-all-2to1-topics`
- `--bridge-all-topics`

## Related project links
* [pilz_robots](http://wiki.ros.org/pilz_robots) package and tutorials for getting started with PRBT6 robot manipulator module
* [jog_arm, currently in moveit_experimental](https://github.com/ros-planning/moveit) used for jogging the manipulator
  best used together with
  [tork-a/fake_joint](https://github.com/tork-a/fake_joint) if testing jogging in a simulation environment.
* TODO: evaluate [tork-a/jog_control](https://github.com/tork-a/jog_control)?!
* [ros-teleop/teleop_twist_keyboard](https://github.com/ros-teleop/teleop_twist_keyboard/),
  see [#16](https://github.com/ros-teleop/teleop_twist_keyboard/pull/16) there for 6D-extension
* [ros-teleop/teleop_tools](https://github.com/ros-teleop/teleop_tools)
