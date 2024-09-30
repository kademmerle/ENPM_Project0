from setuptools import setup

package_name = 'tb_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kyle',
    maintainer_email='kdemmerl@umd.edu',
    description='ENPM662-0201 Project 0 -- Turtlebot3 Controller',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'tb_openLoop = tb_control.tb_openLoop:main'
        ],
    },
)
