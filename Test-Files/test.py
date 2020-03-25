import platform

#Architecture
print("Architecture: " + platform.architecture()[0])

#Machine
print("Machine: " + platform.machine())

#Node
print("Node: " + platform.node())
#System
print("System: " + platform.system())

#Processor
print("Processors: ")
with open("/proc/cpuinfo", "r") as f:
    info =f.readlines()

cpuinfo = [x.strip().split(":")[1] for x in info if "model name" in x]
for index, item in enumerate(cpuinfo):
    print("    " + str(index)+ ": " + item)

# Load
with open("/proc/loadavg","r") as f:
    print("Average Load: " + f.read().strip())
    
#Memory
print("Memory info: ")
with open("/proc/meminfo", "r") as f:
    lines =f.readlines()
print("    " + lines[0].strip())
print("    " + lines[1].strip())

#Uptime
uptime = None
with open("/proc/uptime", "r") as f:
    uptime = f.read().split(" ")[0].strip()
uptime = int(float(uptime))
uptime_hours = uptime // 3600
uptime_minutes = (uptime % 3600) // 60
print("Uptime: " +str(uptime_hours) + ":" +str(uptime_minutes) + " hours")

