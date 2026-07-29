import subprocess

def get_logs(service):
    try:
        result = subprocess.run(["journalctl", "-u", service, "-n", "20", "--no-pager"],
                                 capture_output = True, 
                                 text = True, 
                                 timeout = 5)
    except FileNotFoundError:
        return None
    
    logs = result.stdout.strip()
    return logs if logs else "logs not found"

def show_logs(service):
    if not service:
        print("No service given. Usage: logs <service>")
        return 
    
    logs = get_logs(service)

    if logs is None:
        print("journalctl not found on this machine.")
        return
    
    print(f"=== {service} ===")
    print(logs)






    
