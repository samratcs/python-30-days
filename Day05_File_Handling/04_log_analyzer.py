"""
Read a log file using with open() and count:

INFO
WARNING
ERROR

Example output:

INFO messages: 10
WARNING messages: 3
ERROR messages: 2

"""

print("="*30)
print("File Handling -- Log File Analyzer".center(10))
print("="*30)
info_count = 0
warning_count = 0
error_count = 0
with open("user.log", "r") as file:
    content = file.read()
    print(content)
    lines=content.splitlines()
    for l in lines:
        chunks=l.split()
        if chunks[2] == "INFO":
            info_count += 1
        elif chunks[2] == "ERROR":
            error_count += 1
        elif chunks[2] == "WARNING":
            warning_count += 1

    print("INFO messages:",info_count)
    print("WARNING messages:",warning_count)
    print("ERROR messages:",error_count)