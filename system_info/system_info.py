import platform
import socket
# added import os for cpu count function.
import os
# this function gathers basic info about the sys, like OS, version and name.
import shutil # added import for disk usage info.
def get_system_info():
    info = {}
    info["os"] = platform.system()
    info["os_version"] = platform.version()
    info["hostname"] = socket.gethostname()
    try:
        info["ip_address"] = socket.gethostbyname(info["hostname"])
    except socket.gaierror:
        info["ip_address"] = "Unknown"
   
    cpu_count = os.cpu_count() # added cpu count function to get the number of CPU cores, with error handling for None case.
    info["cpu_count"] = cpu_count if cpu_count is not None else "Unknown"

    total, used, free = shutil.disk_usage("/") #disk function with rounding to 2 decimal places for better readability.
    info["disk_total_gb"] = round(total / (1024**3), 2)
    info["disk_used_gb"] = round(used / (1024**3), 2)
    info["disk_free_gb"] = round(free / (1024**3), 2)

    return info
# prints sys info into a formatted way.
def print_system_info(info):
    print("=== System Info ===")
    print(f"OS: {info['os']} ({info['os_version']})")
    print(f"Hostname: {info['hostname']}")
    print(f"IP Address: {info['ip_address']}")
    print(f"CPU Count: {info['cpu_count']}") 
    print(f"Disk Total: {info['disk_total_gb']} GB")
    print(f"Disk Used:  {info['disk_used_gb']} GB")
    print(f"Disk Free:  {info['disk_free_gb']} GB")


# main function to execute the script and display the sys info.
if __name__ == "__main__":
    sys_info = get_system_info()
    print_system_info(sys_info)
