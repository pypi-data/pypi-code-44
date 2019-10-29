#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = \
['b2constsites']

package_data = \
{'': ['*']}

install_requires = \
['biopython>=1.70', 'pyvcf>=0.6.8']

entry_points = \
{'console_scripts': ['run_b2cs = '
                     'b2constsites.run_b2constsites:run_b2constsites']}

setup(name='b2constsites',
      version='0.3.3',
      description='Generate an appropriate data tag to add constant sites to your BEAST2 XML',
      author='Anders Goncalves da Silva',
      author_email='andersgs@gmail.com',
      url='https://github.com/andersgs/beast2_constsites/',
      packages=packages,
      package_data=package_data,
      install_requires=install_requires,
      entry_points=entry_points,
      python_requires='>=3.6',
     )
