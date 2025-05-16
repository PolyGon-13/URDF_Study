import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
import xacro

def generate_launch_description():
    use_sim_time=LaunchConfiguration("use_sim_time")
    # launch 파일 실행 시 입력받을 수 있는 인자(argument)를 참조

    pkg_path=os.path.join(get_package_share_directory("urdf_tutorial"))
    xacro_file=os.path.join(pkg_path,"urdf","robot_4.xacro")
    robot_description=xacro.process_file(xacro_file)
    params={"robot_description":robot_description.toxml(),"use_sim_time":use_sim_time}
    # use_sim_time:=true 라고 명령을 입력하면 use_sim_time이라는 키로 전달된 true 값을 LaunchConfiguration("use_sim_time")가 평가하여 true값을 robot_state_publisher 노드로 넘겨줌

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "use_sim_time",default_value="false",description="use_sim_time"
            ),
            # 외부로부터 인자를 받을 수 있게 선언하는 역할
            # use_sim_time가 설정되어 있으면 ROS는 시스템 시간이 아니라 /clock 토픽에서 나오는 시뮬레이션 시간을 사용(ROS에서 공통적으로 인식하도록 정해진 관용적인 파라미터)

            Node(
                package="robot_state_publisher",
                executable="robot_state_publisher",
                output="screen",
                parameters=[params],
            ),
        ]
    )