# -*- coding: utf-8 -*-
#
# Copyright (C) 2015-2019 Bitergia
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# Authors:
#   Alvaro del Castillo San Felix <acs@bitergia.com>
#

from .elastic import ElasticOcean


class SupybotOcean(ElasticOcean):
    """MediaWiki Ocean feeder"""

    @classmethod
    def get_perceval_params_from_url(cls, url):
        # In the url the uri and the data dir are included
        params = url.split()

        return params

    @classmethod
    def get_arthur_params_from_url(cls, url):
        # In the url the uri and the dirpath are included

        params = url.split()
        """ Get the arthur params given a URL for the data source """
        params = {"uri": params[0], "dirpath": params[1]}

        return params
