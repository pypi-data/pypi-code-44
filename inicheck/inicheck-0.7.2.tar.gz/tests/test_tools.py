#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test_recipe
----------------------------------

Tests for `inicheck.Tools` module.
"""

import unittest
from inicheck.tools import *
from collections import OrderedDict

class TestTools(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        base = os.path.dirname(__file__)
        self.ucfg = get_user_config(os.path.join(base,"test_configs/full_config.ini"),
                                                            modules="inicheck")

    def test_get_checkers(self):
        """
        Tests the get_checkers func in tools
        """
        checkers = get_checkers().keys()

        valids = ['bool', 'criticaldirectory', 'criticalfilename', 'datetime',
                  'datetimeorderedpair', 'directory', 'filename', 'float',
                  'int', 'string', 'url']

        for v in valids:
            assert v in checkers

        valids = ["type", "generic", "path"]
        checkers = get_checkers(ignore=[]).keys()
        for v in valids:
                assert v in checkers

    def test_check_config(self):
        """
        Tests the check_config func in tools
        """
        ucfg = self.ucfg

        warnings, errors = check_config(ucfg)

        assert len(errors) == 12

    def test_cast_all_variables(self):
        """
        Tests the cast_all_variables func in tools
        """
        ucfg = self.ucfg

        ucfg.cfg['topo']['test_start'] = "10-1-2019"
        ucfg.cfg['air_temp']['dk_ncores'] = "1.0"
        ucfg.cfg['air_temp']['detrend'] = "true"

        ucfg = cast_all_variables(ucfg, ucfg.mcfg)
        results = ['timestamp','int','bool','float','list','str']

        tests = [ucfg.cfg['time']['start_date'],
                  ucfg.cfg['air_temp']['dk_ncores'],
                  ucfg.cfg['air_temp']['detrend'],
                  ucfg.cfg['wind']['reduction_factor'],
                  ucfg.cfg['output']['variables'],
                  ucfg.cfg['air_temp']['distribution']]

        for i,v in enumerate(tests):
            assert results[i] in type(v).__name__.lower()


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
