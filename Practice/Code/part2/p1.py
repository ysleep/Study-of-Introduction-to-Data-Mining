#filename: p1.py

import numpy as np

class Vector:
    def __init__(self,vec):
        self.vec = vec
        self.normalization()

    def normalization(self):
        vec0Mean= self.vec - np.mean(self.vec)
        dist = np.linalg.norm(vec0Mean)
        self.vecNorm = vec0Mean / dist

    def getVecNorm(self):
        return self.vecNorm

def main():
    vec1 = Vector([232,121,165])
    vec2 = Vector([33.5,16.9,24])
    vec3 = Vector([10.7,210.1,427.6])
    x = np.array([vec1.getVecNorm(),vec2.getVecNorm(),vec3.getVecNorm()])
    print np.cov(x)*2

if __name__ == "__main__":
    main()
