# generateKey.py
# Quang Hoang
# 21 OCT 2019

# Generate key

import random

def getKey():

    key = []
    for i in range(1,4):
        key.append(str(random.randint(1,665)))
    key = '-'.join(key)
    return key

