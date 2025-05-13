import os
from ament_index_python.packages import get_package_share_directory # 패키지 안에 있는 파일 경로를 찾을 때 사용
from launch import LaunchDescription # 전체 launch 구성을 담는 객체
from launch.substitutions import LaunchConfiguration # launch 파일 실행 시 넘길 수 있는 인자
from launch.actions import DeclareLaunchArgument # launch 인자 선언
from launch_ros.actions import Node # 실제로 실행할 ROS 노드 지정
import xacro # xacro 파일을 urdf로 변환하기 위해 사용

def generate_launch_description():
    use_sim_time=LaunchConfiguration("use_sim_time") # use_sim_time 이라는 변수를 인자로 사용한다는 의미

    pkg_path=os.path.join(get_package_share_directory("urdf_tutorial"))
    xacro_file=os.path.join(pkg_path,"urdf","robot_2.xacro")
    # urdf_tutorial 패키지의 경로를 가져오고 robot_2.xacro 파일의 전체 경로 제작

    robot_description=xacro.process_file(xacro_file)
    # xacro 파일을 urdf xml으로 변환 : xacro는 xml 매크로 형식이라 그냥 넘기면 안됨

    params={
        "robot_description":robot_description.toxml(), 
        # xacro.process_file로 xacro를 urdf xml로 변환하였다면 여기서는 toxml로 문자열로 바꾸어 파라미터에 넣음
        # ROS에서는 robot_description이라는 파라미터로 urdf를 전달하는 것이 약속. 그래서 해당 노드가 자동으로 찾아서 tf를 계산
        "use_sim_time":use_sim_time,
    }

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "use_sim_time",default_value="false",description="use_sim_time"
            ),
            # use_sim_time 인자를 선언하고 기본값을 false로 지정

            Node(
                package="robot_state_publisher", 
                # package는 실행하고 싶은 노드를 포함하고 있는 패키지를 가져옴
                # robot_state_publisher는 urdf를 읽고 tf를 퍼블리시함
                executable="robot_state_publisher", # 해당 패키지 안에 있는 실제 실행할 노드 선택
                output="screen", # 노드가 출력하는 로그나 메시지를 터미널 화면에 출력
                parameters=[params], # 위에서 만든 파라미터 딕셔너리 전달
            ),
        ]
    )

# ros2 pkg executables [패키지 이름] : 패키지 내의 실행 가능한 노드 검색