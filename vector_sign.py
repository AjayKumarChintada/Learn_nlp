import numpy as np 


p=np.array([1,1])



v=np.array([2,2])
def side_of_plane(plane,vector):
    dot_product=np.dot(plane,vector.T)
    sign_of_dot_product= np.sign(dot_product)
    return sign_of_dot_product


print(side_of_plane(p,np.array([-1,-1])))
print(side_of_plane(p,v))

