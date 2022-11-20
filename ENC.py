import os, platform
try:
    import requests
except:
    os.system('pip install requests')
    os.system('pip install bs4')
    os.system('pip install futures')
    os.system('gut pull')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    import nahid
elif bit == '32bit':
    from nahid import login
    login()
