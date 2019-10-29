"""
Some pipelines used for testing
"""

class ZeroDivisionErrorPipeline(object):

    def open_spider(self, spider):
        a = 1/0

    def process_item(self, item, spider):
        return item


class ProcessWithZeroDivisionErrorPipiline(object):

    def process_item(self, item, spider):
        1/0
