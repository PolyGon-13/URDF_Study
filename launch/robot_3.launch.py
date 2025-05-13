import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
import xacro

def generate_launch_description():
    use_sim_time=LaunchConfiguration("use_sim_time")

    pkg_path=os.path.join(get_package_share_directory("urdf_tutorial"))
    xacro_file=os.path.join(pkg_path,"urdf","robot_3.xacro")
    robot_description=xacro.process_file(xacro_file)
    params={"robot_description":robot_description.toxml(),"use_sim_time":use_sim_time}

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "use_sim_time",default_value="false",description="use_sim_time"
            ),
            Node(
                package="robot_state_publisher",
                executable="robot_state_publisher",
                output="screen",
                parameters=[params],
            ),
        ]
    )

# ros2 run gazebo_ros spawn_entity.py -topic robot_description -entity with_robot
# gazebo_ros 패키지의 Gazebo에 로봇을 생성하는 spawn_entity.py 스크립트 실행
# -topic은 spawn_entity.py 스크립트가 로봇 모델을 읽어올 ROS2 토픽을 지정하는 옵션
# 위에서 만든 robot_description 파라미터를 이용해 로봇을 추가
# -entity는 생성될 로봇의 이름을 지정 : 여기서는 이름을 with_robot으로 지정