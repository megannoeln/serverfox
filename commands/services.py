import subprocess

# loop through services and check whether they are active, inactive, failed, not found
def get_service_status(service):
    try:
        result = subprocess.run(["systemctl", "is-active", service], 
                                capture_output = True, 
                                text = True, 
                                timeout = 5)
    except FileNotFoundError:
        return None
    
    service_status = result.stdout.strip()
    return service_status if service_status else "not found"

# loop and print service status
def show_services(services):
    if not services:
        print("No services given. Enter services command followed by the names of the services you'd like to check")
        return 

    for service in services:
        service_status = get_service_status(service)

        if service_status is None:
            print("systemctl not found on this machine.")
            return

        print(f"{service:<15}{service_status}")
            
