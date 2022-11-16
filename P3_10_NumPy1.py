import numpy as np

def eq(A, B, p):
    return np.sum(A==B)/(np.sum(A!=B)+np.sum(A==B))>=p/100

def closest_point_indexes(points, p):
    return np.arange(points.shape[0])[np.min((points[:, 0]-p[0])**2+(points[:, 1]-p[1])**2)==(points[:, 0]-p[0])**2+(points[:, 1]-p[1])**2]

def number_of_inversions(A):
    return np.sum((np.array([A]*A.shape[0]).T>np.array([A]*A.shape[0])) & (np.array([np.arange(A.shape[0])]*A.shape[0]).T<np.array([np.arange(A.shape[0])]*A.shape[0])))

exec(input().strip())