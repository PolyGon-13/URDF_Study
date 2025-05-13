import os
from ament_index_python.packages import get_package_share_directory # 패키지의 위치를 찾을 때 사용
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription # 다른 launch 파일을 포함할 때 사용
from launch.launch_description_sources import PythonLaunchDescriptionSource # Python 기반의 ROS2 launch 파일을 다른 launch 파일 안에서 실행할 수 있게 해주는 도구
from launch_ros.actions import Node # 노드 실행할 때 사용

def generate_launch_description():
    package_name="urdf_tutorial"

    rsp=IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [os.path.join(get_package_share_directory(package_name),"launch","robot_3.launch.py")]
        ),
        launch_arguments={"use_sim_time":"true"}.items(),
    ) # "launch/robot_3.launch.py"를 가져오고 포함

    gazebo=IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [os.path.join(get_package_share_directory("gazebo_ros"),"launch","gazebo.launch.py")]
        ),
    ) # gazebo를 실행하는 launch 파일을 포함

    spawn_entity=Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=["-topic","robot_description","-entity","with_robot"],
        output="screen",
    ) # gazebo에 로봇을 생성하는 노드

    return LaunchDescription(
        [
            rsp,
            gazebo,
            spawn_entity,
        ]
    )