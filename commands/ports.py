import psutil

# fetch listening tcp ports and corresponding process
def get_ports():
    try:
        tcp_ports = psutil.net_connections(kind="tcp")
    except (psutil.AccessDenied, PermissionError):
        return None

    listening_ports = []

    for connection in tcp_ports:
        if connection.status != psutil.CONN_LISTEN:
            continue

        local_address = connection.laddr.ip if connection.laddr else "unknown"
        local_port = connection.laddr.port if connection.laddr else "unknown"
        process_name = "unknown"

        if connection.pid is not None:
            try:
                process_name = psutil.Process(connection.pid).name()
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                process_name = "unknown"

        listening_ports.append((local_address, local_port, process_name))

    listening_ports.sort(key=lambda port_info: port_info[1])

    return listening_ports

# print local ip, port, process if available
def show_ports():
    ports = get_ports()

    if ports is None:
        print("Ports unavailable: permission denied")
        return

    if not ports:
        print("No listening TCP ports found.")
        return

    print(f"{'PORT':<8}{'ADDRESS':<18}PROCESS")
    for local_address, local_port, process_name in ports:
        print(f"{local_port:<8}{local_address:<18}{process_name}")
