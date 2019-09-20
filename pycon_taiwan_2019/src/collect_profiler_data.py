def traverse(node, stack=[]):
    stack.append(node.key)
    cumtime = node.time
    for child in node.children.values():
        cumtime += traverse(child, stack)
    print(stack, f"{cumtime:.2f}", f"{node.time:.2f}")
    stack.pop()
    return cumtime


import sys, time
from profiler import Profiler
profiler = Profiler(time.time)
import example_abc
sys.setprofile(profiler.callback)
example_abc.run()
sys.setprofile(None)
traverse(profiler.root)