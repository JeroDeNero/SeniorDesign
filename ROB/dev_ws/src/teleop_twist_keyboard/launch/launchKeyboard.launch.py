from launch import LaunchDescription
from launch_ros.actions import Node

# import launch
# import launch.actions
# import launch.substitutions
# import launch_ros.actions

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='teleop_twist_keyboard',
            #node_namespace='launchTest',
            node_executable='teleop_twist_keyboard',
            node_name='teleopKeyboard'
        ),
        Node(
            package='teleop_twist_keyboard',
            #node_namespace='launchTest',
            node_executable='keyboard_subscriber',
            node_name='keyboardSubscriber'
        ),
    ])