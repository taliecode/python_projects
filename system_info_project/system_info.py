import platform
import socket
# added import os for cpu count function.
import os
# this function gathers basic info about the sys, like OS, version and name.
def get_system_info():
    info = {}
    info["os"] = platform.system()
    info["os_version"] = platform.version()
    info["hostname"] = socket.gethostname()
    try:
        info["ip_address"] = socket.gethostbyname(info["hostname"])
    except socket.gaierror:
        info["ip_address"] = "Unknown"
   
    # added cpu count info to the sys info dictionary.
    cpu_count = os.cpu_count()
    info["cpu_count"] = cpu_count if cpu_count is not None else "Unknown"
    return info
# prints sys info into a formatted way.
def print_system_info(info):
    print("=== System Info ===")
    print(f"OS: {info['os']} ({info['os_version']})")
    print(f"Hostname: {info['hostname']}")
    print(f"IP Address: {info['ip_address']}")
    print(f"CPU Count: {info['cpu_count']}") 

# main function to execute the script and display the sys info.
if __name__ == "__main__":
    sys_info = get_system_info()
    print_system_info(sys_info)
