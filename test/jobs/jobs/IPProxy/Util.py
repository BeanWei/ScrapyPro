import random

import ProxiesDataBase
import GetIP
import re

def Refresh():
    GetIP.RefreshDB()
    GetIP.GetIP()

def Get():
    result = ProxiesDataBase.GetItems()
    if result:
        tmp = random.choice(result)
        return 'http://{}'.format(tmp['ip'])
    else:
        print("没有可用IP")
        return None
