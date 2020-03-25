import subprocess
p = subprocess.Popen(["ps", "-a"], stdout=subprocess.PIPE)
out, err = p.communicate()
if ('network-manager' in str(out)):
    print('Httpd running')
if ('mysql' in str(out)):
    print('mysql running')
