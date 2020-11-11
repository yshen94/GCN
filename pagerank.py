
import numpy as np 

w = np.array([0.25,0.25,0.25,0.25])
a = np.array([[0,0.5,1,0],[1/3,0,0,1/2],[1/3, 1/2, 0,0],[1/3,1/2,0,0]])
a_leak = np.array([[0,0,0,1/2],[0,0,0,1/2],[0,1,0,0],[0,0,1,0]])

def work(a, w):
    for i in range(100):
        w = np.dot(a,w)
        print(w)
        
def random_work(a,w,n):
    d = 0.85
    for i in range(100):
        w = (1-d)/n + d*np.dot(a,w)
        print(w)

work(a,w)
#random_work(a,w,4)
#random_work(a_leak,w,4)
#random_work(a_sink,w,4)