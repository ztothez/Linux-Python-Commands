##with open("/proc/diskstats","r") as f:
##    print("Diskstats: " + f.read().strip())
import psutil
def main():
    table = prettytable.PrettyTable(border=False, header=True, left_padding_width=2, padding_width=1)
    table.field_names = ["Device", "Total", "Used", "Free", "Use%", "Type", "Mount"]
    for part in psutil.disk_partitions(all=False):
        if os.name == 'nt':
            if 'cdrom' in part.opts or part.fstype == '':
                # skip cd-rom drives with no disk in it; they may raise
                # ENOENT, pop-up a Windows GUI error for a non-ready
                # partition or just hang.
                continue
        if 'docker' in part.mountpoint and 'aufs' in part.mountpoint:
            continue
        usage = psutil.disk_usage(part.mountpoint)

        table.add_row([part.device,
                       bytes2human(usage.total),
                       bytes2human(usage.used),
                       bytes2human(usage.free),
                       str(int(usage.percent)) + '%',
                       part.fstype,
                       part.mountpoint])
    for field in table.field_names:
        table.align[field] = "l"
    print(table) 
