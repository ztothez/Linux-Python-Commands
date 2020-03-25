import os
from collections import namedtuple

disk_ntuple = namedtuple('partition',  'device mountpoint fstype')
usage_ntuple = namedtuple('usage',  'total used free percent')

all=False
phydevs = []
with open("/proc/filesystems", "r") as f:
    for line in f:
        if not line.startswith("nodev"):
            phydevs.append(line.strip())

retlist = []
with open('/proc/mounts', "r") as f:
    for line in f:
        if not all and line.startswith('none'):
            continue
        fields = line.split()
        device = fields[0]
        mountpoint = fields[1]
        fstype = fields[2]
        if not all and fstype not in phydevs:
            continue
        if device == 'none':
            device = ''
        ntuple = disk_ntuple(device, mountpoint, fstype)
        retlist.append(ntuple.device)
        st = os.statvfs(ntuple.mountpoint)
        free = (st.f_bavail * st.f_frsize)
        total = (st.f_blocks * st.f_frsize)
        used = (st.f_blocks - st.f_bfree) * st.f_frsize
        try:
            percent = ret = (float(used) / total) * 100
        except ZeroDivisionError:
            percent = 0
        print(retlist,usage_ntuple(total, used, free, round(percent, 1)))

