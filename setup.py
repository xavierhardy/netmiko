from distutils.core import setup

setup(
    name='netmiko',
    version='0.2.1',
    url='https://github.com/ktbyers/netmiko',
    download_url='https://github.com/ktbyers/netmiko/archive/v0.2.0.tar.gz',
    license='MIT',
    author='Kirk Byers',
    author_email='ktbyers@twb-tech.com',
    install_requires=['paramiko>=1.13.0', 'scp>=0.10.0'],
    description='Multi-vendor library to simplify Paramiko SSH connections to network devices',
    packages=['netmiko',
              'netmiko/cisco',
              'netmiko/arista',
              'netmiko/hp',
              'netmiko/f5',
              'netmiko/juniper',
              'netmiko/brocade',
              'netmiko/huawei',],
    )

