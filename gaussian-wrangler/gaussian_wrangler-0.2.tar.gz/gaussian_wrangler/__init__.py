"""
tools for creating and analyzing Gaussian files
"""

# Make Python 2 and 3 imports work the same
# Safe to remove with Python 3-only code
from __future__ import absolute_import

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions

__author__ = 'Heather B Mayes'
__email__ = 'hmayes@hmayes.com'
__version__ = '0.0.1'

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
