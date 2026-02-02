'''
Import built-in os module so that the appropriate Operating System
command can be determined.
'''
import os

def clear_screen() -> None:
    """
    A utility function that clears the console
    based according to the host operating system.
    """
    os.system("cls" if os.name == "nt" else "clear")
