import cx_Freeze
import sys
import os

base = None 

if sys.platform=='win32':
    base = "Win32GUI"


executables = [cx_Freeze.Executable("gscScriptCompAndDecompiler.py")]    

cx_Freeze.setup(
        name = "Name",
        options = {"build_exe":{"packages":["tkinter"]}},
        version="1",
        executables=executables) 