#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = \
['solo', 'solo.cli', 'solo.fido2']

package_data = \
{'': ['*']}

install_requires = \
['click >= 7.0',
 'cryptography',
 'ecdsa',
 'fido2 == 0.7.3',
 'intelhex',
 'pyserial',
 'pyusb',
 'requests']

entry_points = \
{'console_scripts': ['solo = solo.cli:solo_cli']}

setup(name='solo-python',
      version='0.0.17',
      description='Python library for SoloKeys.',
      author='SoloKeys',
      author_email='hello@solokeys.com',
      url='https://github.com/solokeys/solo-python',
      packages=packages,
      package_data=package_data,
      install_requires=install_requires,
      entry_points=entry_points,
      python_requires='>=3.6',
     )
