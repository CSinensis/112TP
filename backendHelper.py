from graphClass import *

def cleanCache(cache,target):
    for i in range(len(cache)):
        if cache[i][2] == target:
            seen,cost,current,check,Q = cache[i]
            return cache[:i] + [(seen,cost,current,check,[])]

def cleanBFSCache(cache,target):
    for i in range(len(cache)):
        if cache[i][3] == target:
            seen,path,current,check,Q = cache[i]
            return cache[:i] + [cache[i],(seen,path,target,check,[])]

def h(node,target):
    return (abs(node.x-target.x) + abs(node.y-target.y))