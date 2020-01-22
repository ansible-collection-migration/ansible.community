# -*- coding: utf-8 -*-
# Copyright (c) 2019 Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import pytest

from ansible_collections.ansible.community.plugins.module_utils._text import to_native
from ansible_collections.ansible.community.plugins.module_utils.common.validation import check_type_str


TEST_CASES = (
    ('string', 'string'),
    (100, '100'),
    (1.5, '1.5'),
    ({'k1': 'v1'}, "{'k1': 'v1'}"),
    ([1, 2, 'three'], "[1, 2, 'three']"),
    ((1, 2,), '(1, 2)'),
)


@pytest.mark.parametrize('value, expected', TEST_CASES)
def test_check_type_str(value, expected):
    assert expected == check_type_str(value)


@pytest.mark.parametrize('value, expected', TEST_CASES[1:])
def test_check_type_str_no_conversion(value, expected):
    with pytest.raises(TypeError) as e:
        check_type_str(value, allow_conversion=False)
    assert 'is not a string and conversion is not allowed' in to_native(e.value)
