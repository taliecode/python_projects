import platform
import socket
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
    return info
# prints sys info into a formatted way.
def print_system_info(info):
    print("=== System Info ===")
    print(f"OS: {info['os']} ({info['os_version']})")
    print(f"Hostname: {info['hostname']}")
    print(f"IP Address: {info['ip_address']}")
# main function to execute the script and display the sys info.
if __name__ == "__main__":
    sys_info = get_system_info()
    print_system_info(sys_info)
