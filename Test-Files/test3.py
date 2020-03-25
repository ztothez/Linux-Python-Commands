import subprocess
output = subprocess.check_output(['ps', '-A'])
if 'Network-Manager' in output:
    print("Httpd is up an running!")
