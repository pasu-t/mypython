# import paramiko
# ip='10.49.20.152'
# port=22
# username = 'root' 
# password = 'adtran1234'

# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(ip,port,username,password)
# stdin,stdout,stderr=ssh.exec_command('ls')
# outlines=stdout.readlines()
# resp=''.join(outlines)
# print(resp)
import subprocess
import sys
from fabric import Connection
print(help(Connection))
result = Connection('10.49.20.156').run('uname -s', hide=True)
print(result)