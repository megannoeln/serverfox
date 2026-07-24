import platform
import socket
import getpass

def get_identity():
    return platform.platform(), socket.gethostname(), getpass.getuser()

def show_identity():
    operating_system, hostname, user = get_identity()

    print(f"Operating system: {operating_system}")
    print(f"Hostname: {hostname}")
    print(f"Current user: {user}")