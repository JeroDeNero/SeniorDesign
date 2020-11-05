from launch import LaunchDescription
from launch_ros.actions import Node

# import launch
# import launch.actions
# import launch.substitutions
# import launch_ros.actions

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='py_pubsub',
            #node_namespace='launchTest',
            node_executable='talker',
            node_name='talker'
        ),
        Node(
            package='py_pubsub',
            #node_namespace='launchTest',
            node_executable='listener',
            node_name='listener'
        ),
        # Node(
        #     package='turtlesim',
        #     node_executable='mimic',
        #     node_name='mimic',
        #     remappings=[
        #         ('/input/pose', '/turtlesim1/turtle1/pose'),
        #         ('/output/cmd_vel', '/turtlesim2/turtle1/cmd_vel'),
        #     ]
        # )
    ])