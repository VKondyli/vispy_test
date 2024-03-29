import numpy as np
from vispy import io
from vispy.util import transforms as tr

np.set_printoptions(suppress=True, precision=2)



class Mesh:

    def __init__(self, obj_filename, position, rotation, scale):
        vertices, faces, normals, texcoords = io.read_mesh(obj_filename)
        assert len(vertices[0]) == 3, "Vertices are 3D"
        assert len(faces[0]) == 3, "Mesh mush be triangulated"
        self.vertices = vertices
        self.faces = faces
        self.postion = position
        self.rotation = rotation
        self.scale = scale

    @property
    def model_matrix(self):
        return make_model_matrix(self.position, self.rotation, self.scale)




def model_matrix(self):

    """
    Rreturn a 4x4 model matrixself.

    Arguments:
     - translation : x,y,z coordinates
     - rotation: x,y,z  rotation (degrees)
     - scale x,y,z  scaleself.

    Returns:
     - model_matrix: 4x4 array
    """


    sm = tr.scale(self.scale).T
    rx, ry,rz = self.rotation
    rzm = tr.rotate(rz,[0,0,1]).T
    rym = tr.rotate(ry,[0,1,0]).T
    rxm = tr.rotate(rx,[1,0,0]).T
    trm = tr.translate(self.translate).T
    mm= trm @ rxm @ rym @ rzm @ sm
    return mm






cup = Mesh('cup1.obj', position=[1,2,3], rotation=[90, 45, 0], scale=[2,2,2])
#print(cup.faces)
#print(cup.vertices)
#cup.position
print(cup.model_matrix)
#cup.send()
#cup.draw()
cup.position = [3,3,3]

#"print('Hello!')"
mm = make_model_matrix([1,2,3], [90,45,0], [2,2,2])
#print(mm)


#"print (vertices[0])"
#"print (len(vertices[0]))"
