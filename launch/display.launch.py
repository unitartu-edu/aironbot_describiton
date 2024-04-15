from ament_index_python.packages import get_package_share_directory
import os
from launch import LaunchDescription
from launch.substitutions import Command
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    pkg_dir = get_package_share_directory('aironbot_description')
    robot_description = os.path.join(pkg_dir, 'urdf/aironbot.urdf')

    ld.add_action(Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': Command(['xacro ', robot_description])}]
    ))

    ld.add_action(Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui'
    ))

    ld.add_action(Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d' + os.path.join(pkg_dir, 'config', 'aironbot_model.rviz')],
    ))

    return ld
