# -*- coding: utf-8 -*-
import pytest

from bolt import HTB_SPC
from bolt import htb_spec


def test_bolt_object():
    assert HTB_SPC['M16']['Qal'] == 30.2
    assert htb_spec(size='M16', type='Q', term='LONG') == 30.2
