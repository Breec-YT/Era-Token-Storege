import os
import subprocess
try:
    if os.path.isfile('Logintoken.txt'):
        with open('Logintoken.txt', 'r') as file:data = file.read()
        os.system('echo | set /p nul=' + data.strip() + '| clip')
    else:open('Logintoken.txt', 'a').close()
    subprocess.Popen("FortniteLauncher.exe")
except:
    pass
