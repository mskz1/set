# -*- coding: utf-8 -*-
import pytest

# from bolt import HTB_SPC
from bolt import htb_spec


# from bolt import K



def test_bolt_object():
    # assert HTB_SPC['M16']['Qal'] == 30.2
    # assert HTB_SPC[K.M16][K.Qal] == 30.2
    # assert htb_spec(size=K.M16, type=K.Qal) == 30.2
    assert htb_spec(size='M16', prop='QA', term='LONG') == 30.2
