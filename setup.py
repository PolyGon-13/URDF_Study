import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'urdf_tutorial'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    # packages=find_packages(exclude=['test']),
    # find_packages는 현재 디렉토리에서 __init__.py 파일이 있는 모든 디렉토리를 찾아서 Python 패키지로 자동 인식해 리스트로 반환
    # exclude를 사용하면 해당 폴더만 제외하고 Python 패키지로 포함시킴
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name,'launch'),glob('launch/*.launch.py')),
        (os.path.join('share',package_name,'urdf'),glob('urdf/*.xacro')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='polygon',
    maintainer_email='hyundiego@hanyang.ac.kr',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'topic_filter=urdf_tutorial.topic_filter:main',
        ],
    },
)
