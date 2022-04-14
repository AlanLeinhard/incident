
from subprocess import Popen, PIPE

def call_cmd(cmd):
    proc = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True, encoding='utf-8')
    stdout, stderr = proc.communicate()
    out = stdout + stderr
    return out

user = call_cmd('cd /media && ls')
print(call_cmd('cd /media/alan && ls'))