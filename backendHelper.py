from graphClass import *

def cleanCache(cache,target):
    for i in range(len(cache)):
        if cache[i][2] == target:
            return cache[:i] + [cache[i]]