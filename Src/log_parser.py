# Log parsing automation

error_keywords = ["ERROR", "CRITICAL", "WARNING"]

log_file = "app.log"

print("Scanning log file for issues...")
print("------------------------------")

with open(log_file, "r") as file:
    for line in file:
        for keyword in error_keywords:
            if keyword in line:
                print(line.strip())
