import ctypes
import os
import sys

def run_as_admin(script_path):
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{script_path}"', None, 1)

if __name__ == "__main__":
    # Specify the path to your original script and any arguments
    original_script_path = r"youtube_to_text.py"
    original_script_args = ["arg1", "arg2"]  # Add your script arguments here

    # Check if the script is already running with administrator privileges
    if ctypes.windll.shell32.IsUserAnAdmin() == 0:
        run_as_admin(original_script_path)
    else:
        # Run your original script here (assuming it doesn't require admin privileges)
        os.system(f'python "{original_script_path}" {" ".join(original_script_args)}')
