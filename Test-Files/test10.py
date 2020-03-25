import os
mounts = self, detectdev=False
mounts = []
with open('/proc/mounts', 'r') as f:
    for line in f:
        dev, path, fstype = line.split()[0:3]
        if fstype in ('ext2', 'ext3', 'ext4', 'xfs',
                      'jfs', 'reiserfs', 'btrfs',
                      'simfs'): # simfs: filesystem in OpenVZ
            if not os.path.isdir(path): continue
            mounts.append({'dev': dev, 'path': path, 'fstype': fstype})
for mount in mounts:
    stat = os.statvfs(mount['path'])
    total = stat.f_blocks*stat.f_bsize
    free = stat.f_bfree*stat.f_bsize
    used = (stat.f_blocks-stat.f_bfree)*stat.f_bsize
    mount['total'] = b2h(total)
    mount['free'] = b2h(free)
    mount['used'] = b2h(used)
    mount['used_rate'] = div_percent(used, total)
    if detectdev:
        dev = os.stat(mount['path']).st_dev
        mount['major'], mount['minor'] = os.major(dev), os.minor(dev)
print(mounts)

