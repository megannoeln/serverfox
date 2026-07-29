import sys
from commands.health import show_health
from commands.network import show_network_info
from commands.services import show_services
from commands.logs import show_logs
from commands.ports import show_ports

def show_help():
    print("Serverfox commands:")
    print("  health    Show a system health snapshot")
    print("  net       Show basic network connectivity info")
    print("  services  Check one or more systemd services")
    print("  logs      Show recent logs for one service")
    print("  ports     Show listening TCP ports")

def main():
    if len(sys.argv) <= 1:
        show_help()
    elif sys.argv[1] == "health":
        show_health()
    elif sys.argv[1] == "net":
        show_network_info()
    elif sys.argv[1] == "services":
        show_services(sys.argv[2:])
    elif sys.argv[1] == "logs":
        service = sys.argv[2] if len(sys.argv) >= 3 else None
        show_logs(service)
    elif sys.argv[1] == "ports":
        show_ports()
    else:
        show_help()

if __name__ == "__main__":
    main()
