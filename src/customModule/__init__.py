# Importing specific functions from local files (file1 and file2)
from .file1 import greet 
from .file2 import farewell
# Declaring the public API of the module to include only greet and farewell
__all__=["greet","farewell"]