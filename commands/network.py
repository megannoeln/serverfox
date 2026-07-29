import socket

# find and return the local ip address
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
    except PermissionError:
        return "unavailable: permission denied"
    finally:
        s.close()

    return local_ip

# return whether the machine can reach the internet
def can_reach_internet():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False

# print network info
def show_network_info():
    ip_addr = get_local_ip()
    internet_status = "reachable" if can_reach_internet() else "unreachable"

    print(f"Local IPv4: {ip_addr}")
    print(f"Internet: {internet_status}")
