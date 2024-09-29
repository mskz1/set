from section.steel import *
import json


def test_section_1():
    s = Profile()
    print()
    print(vars(s))
    print(json.dumps(vars(s), indent=4))
