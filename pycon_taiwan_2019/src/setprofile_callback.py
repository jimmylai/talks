def callback(frame, event, arg):
    func_name = frame.f_code.co_name if frame and frame.f_code and frame.f_code.co_name else None
    print(func_name, event)

import example_abc
import sys
sys.setprofile(callback)
example_abc.run()
sys.setprofile(None)
