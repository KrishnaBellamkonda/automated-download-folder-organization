# Setup File 
from cx_Freeze import setup, Executable

# The pacakges included in the program 
packages = ["os", "shutil", "time", "watchdog", "pathlib"]

# Creating the options dict (like JSON object) 
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

# The main program that is to be executed
executables = [Executable("organizer.py", base=None)] # Declaring organizer as executable

# Build the exe file 
setup(
    name = "orgaizer",
    options = options,
    version = "0.1",
    description = 'A simple script that helps you organize your Downloads folder',
    executables = executables
)