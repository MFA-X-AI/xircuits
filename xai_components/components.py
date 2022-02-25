from xpressai import *

class MyComponent(Component):
    data_name: InArg[str]
    data_set: OutArg[Dataset]
    name: InArg[str]
        
    def __init__(self, ctx):
        self.data_name = InArg.default()
        self.data_set = OutArg.default()
        
    def execute(self):
        # logic here
        pass

class RotateCounterClockWiseComponent(Component):
    data_set: InArg[Dataset]
    out: OutArg[Dataset]
        
    def execute(self):
        pass
    