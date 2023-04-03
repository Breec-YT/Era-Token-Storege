import os
try:
    if os.path.isfile('Logintoken.txt'):
        with open('Logintoken.txt', 'r') as file:data = file.read()
        os.system('echo | set /p nul=' + data.strip() + '| clip')
    else:open('Logintoken.txt', 'a').close()
    os.system('FortniteLauncher.exe')
except:
    pass