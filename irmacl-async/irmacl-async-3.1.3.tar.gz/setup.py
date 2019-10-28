# Copyright (c) 2013-2019 Quarkslab.
# This file is part of IRMA project.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the top-level directory
# of this distribution and at:
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# No part of the project, including this file, may be copied,
# modified, propagated, or distributed except according to the
# terms contained in the LICENSE file.


from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='irmacl-async',
    version='3.1.3',
    description='Irma asynchronous command line tool for API v3',
    long_description=readme(),
    url='https://github.com/quarkslab/irmacl-async',
    author='irma-dev',
    author_email='irma-dev@quarkslab.com',
    license='ApacheV2',
    packages=['irmacl_async'],
    install_requires=(
        'aiohttp==3.3.2',
        'irma-shared==3.2.1',
        'pyyaml'
    ),
    include_package_data=True,
    test_suite='tests',
    tests_require=(
        'asynctest',
    ),
    zip_safe=False
)
