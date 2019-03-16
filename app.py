import numpy as np
from mesh_delgrosso import Mesh
from vispy import app, gloo
np.set_printoptions(suppress=True, precision=2)



#import mesh
cup = Mesh('cup1.obj', position=[10, 2, 3], rotation=[90, 45, 0], scale=[2, 2, 2])
print(cup.model_matrix)
print(cup.position)


#make window
canvas =app.Canvas(keys='interactive')



@canvas.connect
def on_draw(event):
    gloo.clear([1,0,1])
    canvas.update()

#show wino, run program
canvas.show()
app.run()
