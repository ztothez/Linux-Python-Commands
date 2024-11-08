import os
import time
import dbus
import psutil

# Configuration for each module
config = {
    "service_status": {
        "alert_status": "inactive",
        "alert_interval": 60,
        "poll_interval": 60
    },
    "disk_info": {
        "alert_percent": 2,
        "alert_interval": 60,
        "poll_interval": 60,
        "Physical_Disk_Only": False
    },
    "load_usage": {
        "alert_percent": 5,
        "alert_interval": 60,
        "poll_interval": 60
    },
    "memory_info": {
        "alert_percent": 100,
        "alert_interval": 60,
        "poll_interval": 60
    }
}

ALERT_TIME = {}

def service_status():
    try:
        service = 'man-db'
        bus = dbus.SystemBus()
        systemd = bus.get_object('org.freedesktop.systemd1', '/org/freedesktop/systemd1')
        manager = dbus.Interface(systemd, 'org.freedesktop.systemd1.Manager')
        service_unit = service if service.endswith('.service') else manager.GetUnit(f'{service}.service')
        service_proxy = bus.get_object('org.freedesktop.systemd1', str(service_unit))
        service_properties = dbus.Interface(service_proxy, dbus_interface='org.freedesktop.DBus.Properties')
        
        load_state = service_properties.Get('org.freedesktop.systemd1.Unit', 'LoadState')
        active_state = service_properties.Get('org.freedesktop.systemd1.Unit', 'ActiveState')
        
        print(f"Load State: {load_state}")
        print(f"Active State: {active_state}")
    except Exception as e:
        print(f"Error retrieving service status: {e}")

def disk_info():
    partitions = psutil.disk_partitions(all=True)
    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        print(f"Device: {partition.device}")
        print(f"  Total: {usage.total} bytes")
        print(f"  Used: {usage.used} bytes")
        print(f"  Free: {usage.free} bytes")
        print(f"  Percent Used: {usage.percent}%")
        print()

def load_usage():
    try:
        with open("/proc/loadavg", "r") as f:
            lines = f.readline().split()
            core_load = float(lines[0])

        with open("/proc/cpuinfo", "r") as f:
            core_count = f.read().split('cpu cores\t: ')[1].split('\n')[0]
            core_number = int(core_count)
        
        core_usage = (core_load / core_number) * 100
        print(f"Core Load: {core_load}")
        print(f"Core Count: {core_number}")
        print(f"Core Usage: {core_usage:.2f}%")
    except Exception as e:
        print(f"Error calculating load usage: {e}")

def memory_info():
    try:
        with open("/proc/meminfo", "r") as f:
            lines = f.readlines()
            mem_total = int(lines[0].split()[1])
            mem_free = int(lines[1].split()[1])
            mem_available = int(lines[2].split()[1])
            usage_percentage = (mem_available / mem_total) * 100

            print(f"Total Memory: {mem_total} kB")
            print(f"Free Memory: {mem_free} kB")
            print(f"Available Memory: {mem_available} kB")
            print(f"Memory Usage: {usage_percentage:.2f}%")
    except Exception as e:
        print(f"Error retrieving memory info: {e}")

# Main menu to select options
def main_menu():
    while True:
        print("\nSelect the function to run:")
        print("1. Service Status")
        print("2. Disk Info")
        print("3. Load Usage")
        print("4. Memory Info")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            service_status()
        elif choice == '2':
            disk_info()
        elif choice == '3':
            load_usage()
        elif choice == '4':
            memory_info()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
