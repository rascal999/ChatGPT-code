#!/usr/bin/env python3

import inspect

# Get the source code of the script
script_source = inspect.getsource(inspect.currentframe())

# Print the source code of the script
print(script_source)
