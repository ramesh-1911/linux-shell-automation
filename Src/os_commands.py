import platform
import subprocess

def run_command(command):
    try:
        result = subprocess.run(
            command,
            shell=True,
            text=True,
            capture_output=True
        )
        return result.stdout.strip()
    except Exception as error:
        return f"Error: {error}"

print("Operating System:", platform.system())

if platform.system() == "Windows":
    print("Current User:")
    print(run_command("whoami"))

    print("\nSystem Info:")
    print(run_command("systeminfo | find \"OS Name\""))
else:
    print("Current User:")
    print(run_command("whoami"))

    print("\nSystem Info:")
    print(run_command("uname -a"))
