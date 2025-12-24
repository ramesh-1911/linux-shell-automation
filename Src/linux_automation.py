import subprocess
import platform

def run_command(command):
    try:
        result = subprocess.run(
            command,
            shell=True,
            text=True,
            capture_output=True
        )
        return result.stdout.strip()
    except Exception as e:
        return str(e)

print("Operating System:", platform.system())
print("Uptime:")
print(run_command("uptime"))

print("\nDisk Usage:")
print(run_command("df -h"))

print("\nMemory Usage:")
print(run_command("free -h"))
print("\nActive Network Connections:")
print(run_command("ss -tuln"))