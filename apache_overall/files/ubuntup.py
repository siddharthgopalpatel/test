import subprocess

a1 = subprocess.check_output("ps -ef | grep -i apache2 | grep -v grep | wc -l", shell=True)
a2 = subprocess.check_output("ps -ef | grep -i sshd | grep -v grep | wc -l", shell=True)

if (int(a1)==3 and int(a2)==3):
    print("All processes are up and running")
elif (int(a1)==3 and int(a2)!=3):
    print("SSHD process is not running")
elif (int(a1)!=3 and int(a2)==3):
    print("Apache2 process is not running")
elif (int(a1)!=3 and int(a2)!=3):
    print("Apache2 and SSHD processes are not running") 
