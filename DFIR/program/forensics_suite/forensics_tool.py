import os
import subprocess

def main():
     # Check OS environment
    os_name = os.name

    if os_name == "nt":  # Windows
        print("Executing Windows program...")
        # Replace this with your actual Windows program execution code
        # (e.g., calling external commands, running specific functions)
    elif os_name == "posix":  # Linux and other Unix-like systems
        print("Executing Linux program...")
        # Replace this with your actual Linux program execution code
    else:
        print(f"Unsupported OS: {os_name}")

if __name__ == "__main__":
    main()


def open_application(application_path):
    """Opens an application using subprocess.Popen (Windows, Linux).

    Args:
        application_path: The path to the application executable.
    """
    
    try:
        subprocess.Popen([application_path])
    except FileNotFoundError:
        print(f"Error: Application '{application_path}' not found.")