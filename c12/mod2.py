import os
import mod1
# from . import mod1

if os.getenv("UNIT_TEST"):
    import fake_mod1 as mod1
else:
    import mod1

def summer(x: int, y:int):
    return mod1.preamble() + f"{x + y}"
