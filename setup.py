from glob import glob
from setuptools import setup

package_name = 'ur5e_voice_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],

    # Install shared files (ROS2)
    data_files=[
        # Register package in ament index
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),

        # Install package.xml
        ('share/' + package_name,
         ['package.xml']),

        # Install all launch files
        ('share/' + package_name + '/launch',
         glob('launch/*.launch.py')),

        #Install config
        ('share/' + package_name + '/config',[
            'config/initial_positions.yaml',
            'config/ur5e_executor_params.yaml',
        ]),
    ],

    install_requires=['setuptools'],
    zip_safe=True,

    # Package metadata
    maintainer='thawatchai',
    maintainer_email='example@example.com',
    description='UR5 simulation and control tools',
    license='Apache License 2.0',
    tests_require=['pytest'],

    # ROS2 Console Scripts (Nodes)
    entry_points={
        'console_scripts': [
            # Speech & Voice
            'speech_to_text_node = ur5e_voice_control.speech_to_text_node:main',
            'tts_node_gtts = ur5e_voice_control.tts_node_gtts:main',
            'speech_gui_node = ur5e_voice_control.speech_gui_node:main',
            'nlu_parser_node = ur5e_voice_control.nlu_parser_node:main',
            'beep_node = ur5e_voice_control.beep_node:main',
            'voice_logger_node = ur5e_voice_control.voice_logger_node:main',
            'dialog_fsm_node = ur5e_voice_control.dialog_fsm_node:main',
            'audio_monitor_gui = ur5e_voice_control.audio_monitor_gui:main',
            
            # UR5 Control
            'ur5_cmd_mapper_node = ur5e_voice_control.ur5_cmd_mapper_node:main',
            'control_position_node = ur5e_voice_control.control_position_node:main',
            'ur5_executor_node = ur5e_voice_control.ur5_executor_node:main',
            'gripper_bridge_node = ur5e_voice_control.gripper_bridge_node:main',

        ],
    },
)
