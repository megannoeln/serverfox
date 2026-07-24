import psutil
from datetime import datetime
from commands.identity import show_identity

gb = 1024 ** 3

# return cpu usage and load average 
def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    load_1, load_5, load_15 = psutil.getloadavg()
    load_average = f"{load_1:.2f}, {load_5:.2f}, {load_15:.2f}"

    return cpu_usage, load_average

# return memory usage
def check_memory():
    memory = psutil.virtual_memory()

    memory_usage = memory.percent
    total_memory = memory.total / gb
    available_memory = memory.available / gb

    return memory_usage, total_memory, available_memory

# return disk usage
def check_disk():
    disk = psutil.disk_usage("/")

    total_disk_space = disk.total / gb
    free_disk_space = disk.free / gb
    disk_usage_percent = disk.percent

    return disk_usage_percent, free_disk_space, total_disk_space

# return uptime
def check_uptime():
    try:
        boot_time_timestamp = psutil.boot_time()
    except PermissionError: 
        return "unavailable: permission denied"

    boot_time = datetime.fromtimestamp(boot_time_timestamp)
    uptime = str(datetime.now() - boot_time).split(".")[0]
    return uptime

# return overall status of machine health, in order of importance
def check_status(cpu_usage, memory_usage, disk_usage):
    if disk_usage >= 90:
        return "Critical", "Disk usage is high"
    elif disk_usage >= 80:
        return "Warning", "Disk usage is moderately high"
    
    if memory_usage >= 90:
        return "Critical", "Memory usage is high"
    elif memory_usage >= 75:
        return "Warning", "Memory usage is moderately high"
    
    if cpu_usage >= 90:
        return "Critical", "CPU usage is high"
    elif cpu_usage >= 70:
        return "Warning", "CPU usage is moderately high"
    
    return "Healthy", None

# gather and print out all health metrics
def show_health():
    cpu_usage, load_average = check_cpu()
    memory_usage, total_memory, available_memory = check_memory()
    disk_usage_percent, free_disk_space, total_disk_space = check_disk()
    uptime = check_uptime()
    status, cause = check_status(cpu_usage, memory_usage, disk_usage_percent)

    print("")
    show_identity()
    print("---------------------")
    print(f"CPU: {cpu_usage}%")
    print(f"Load (1m, 5m, 15m): {load_average}")
    print(f"RAM: {memory_usage}% used, {round(available_memory, 2)}gb free of {round(total_memory, 2)}gb")
    print(f"Disk: {disk_usage_percent}% used, {round(free_disk_space, 2)}gb free of {round(total_disk_space, 2)}gb")
    print(f"Uptime: {uptime}")
    print("---------------------")
    if cause:
        print(f"Status: {status}, Cause: {cause}")
    else:
        print(f"Status: {status}")