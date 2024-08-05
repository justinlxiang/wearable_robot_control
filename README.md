# MindRove Package

## Overview

This is a ROS1 package designed to interface with the MindRove Armband. The package processes data from the armband's 8 EMG channels and 6 IMU channels (Gyroscope and Accelerometer) to detect a double_squeeze trigger and perform gesture classification. Based on the detected gestures, the package can execute various robot commands, which can be customized in the `command_center.py` script.

## Requirements

The required dependencies for this package are listed in the `requirements.txt` file. To install them, you can use the following command:
```bash
pip install -r requirements.txt
```


## Features

- **Double Squeeze Trigger**: The package can detect a double squeeze gesture to activate the command listening mode. This allows the system to start listening for subsequent gesture commands to execute.
- **Gesture Classification**: The package can classify different gestures such as wave, push, squeeze, point, and thumb_up.
- **Customizable Commands**: Users can customize the robot commands associated with each gesture in the `command_center.py` script.
- **Robot Control**: The package can send navigation goals, change LED colors, and play sounds based on the classified gestures.

## Installation

1. Ensure you have ROS1 installed on your system.
2. Clone this repository into your ROS workspace:
    ```bash
    cd ~/catkin_ws/src
    git clone <repository_url>
    ```
3. Build the package:
    ```bash
    cd ~/catkin_ws
    catkin_make
    ```

## Usage

1. Source your ROS workspace:
    ```bash
    source ~/catkin_ws/devel/setup.bash
    ```
2. Launch the program with the launch file:
    ```bash
    roslaunch lauch mindrove_launch.launch
    ```

## Customizing Commands

The `command_center.py` script contains the logic for handling different gestures. You can customize the commands by modifying the `callback` function in the script.

