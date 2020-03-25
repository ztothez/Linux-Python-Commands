import os
import sys

service = "network-manager"

p =  os.popen(["systemctl", "is-active",  service])
(output, err) = p.communicate()
output = output.decode('utf-8')

print(output)
