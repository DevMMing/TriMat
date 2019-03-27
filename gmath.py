import math
from display import *



#vector functions
#normalize vector, should modify the parameter
def normalize(vector):
    length = math.sqrt(math.pow(vector[0],2)+math.pow(vector[1],2)+math.pow(vector[2],2))
    vector[0]/=length
    vector[1]/=length
    vector[2]/=length
    return vector
#Return the dot porduct of a . b
def dot_product(a, b):
    return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):
    p0=polygons[i]
    p1=polygons[i+1]
    p2=polygons[i+2]
    a=[p1[0]-p0[0],p1[1]-p0[1],p1[2]-p0[2]]
    b=[p2[0]-p1[0],p2[1]-p1[1],p2[2]-p1[2]]
    n=[a[2]*b[3]-a[3]*b[2],a[3]*b[1]-a[1]*b[3],a[1]*b[2]-a[2]*b[1]]
    return n
