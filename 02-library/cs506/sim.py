import math

def euclidean_dist(x, y):
    if (len(x)==0 or len(y)==0):
        return ValueError("Vector cannot be empty!")
    if (len(x)!= len(y)):
        return ValueError("Vector must be in the same dimension!")
    sum = 0.
    entdis = 0.
    entdis_2 = 0.
    for i in range(len(x)):
        entdis = abs(x[i]-y[i])
        entdis_2 = entdis**2
        sum +=entdis_2
    return (sum**0.5)

def manhattan_dist(x, y):
    if(len(x)==0 or len(y)==0):
        return ValueError("Vectors cannot be empty!")
    if (len(x)!=len(y)):
        return ValueError("Vectors must be in the same dimension!")
    sum = 0.
    entdis = 0.
    for i in range(len(x)):
        entdis = abs(x[i]-y[i])
        sum += entdis
    return sum   

def jaccard_dist(x, y):
    if (len(x)==0 or len(y)==0):
        return ValueError("Vector cannot be empty!")
    if (len(x)!=len(y)):
        return ValueError("Vector must be in the same dimension!")
    
    cap = set(x).intersection(set(y))
    cup = set(x).union(set(y))
    return 1-((abs(len(cap))))/(abs(len(cup)))   

def cosine_sim(x, y):
    if (len(x)==0 or len(y)==0):
        return ValueError("Vector cannot be empty!")
    if (len(x)!=len(y)):
        return ValueError("Vector must be in the same dimension!")
    
    normx = 0.
    normxsq = 0.
    normy = 0.
    normysq = 0.
    dorprdc = 0.
    for i in range(len(x)):
        normxsq += x[i]**2
        normysq += y[i]**2
        normx += normxsq**.5
        normy += normysq**.5
        dotprodc += x[i]*y[i]
    return (dotproc/(normx*normy)
    
# Feel free to add more
