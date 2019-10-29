# -*- coding: utf-8 -*-

from great_expectations.render.renderer.content_block.expectation_string import ExpectationStringRenderer


class ExpectationSuiteBulletListContentBlockRenderer(ExpectationStringRenderer):
    _content_block_type = "bullet_list"

    _default_element_styling = {
        "default": {
            "classes": ["badge", "badge-secondary"]
        },
        "params": {
            "column": {
                "classes": ["badge", "badge-primary"]
            }
        }
    }

