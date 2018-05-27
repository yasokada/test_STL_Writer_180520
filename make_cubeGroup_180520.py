import numpy as np
import sys

import STLWriter as STLWR
# STLWriter
# code from
# http://code.activestate.com/recipes/578246/
# by Manfred Moitzi
# (renamed as STLWriter.py from recipe-578246-1.py)

#

'''
v0.2 May, 27, 2018
  - change [DIPOLE_SIZE]
  - change [OUT_FILE]
v0.1 May, 20, 2018
  - read dipole positions from [IN_FILE]
  - add python_list_add()
  - get_cube() takes [size] arg
  - add make_cubeGroup()
'''


def python_list_add(in1, in2):
    wrk = np.array(in1) + np.array(in2)
    return wrk.tolist()


def make_cubeGroup():
    def get_cube(size=3, origin=[0, 0, 0]):
        # cube corner points
        s = size
        p1 = python_list_add(origin, (0, 0, 0))
        p2 = python_list_add(origin, (0, 0, s))
        p3 = python_list_add(origin, (0, s, 0))
        p4 = python_list_add(origin, (0, s, s))
        p5 = python_list_add(origin, (s, 0, 0))
        p6 = python_list_add(origin, (s, 0, s))
        p7 = python_list_add(origin, (s, s, 0))
        p8 = python_list_add(origin, (s, s, s))

        print(p1)

        # define the 6 cube faces
        # faces just lists of 3 or 4 vertices
        #
        # [NOTE]
        # vertices must be defined [anticlockwise] to be seen on GitHub
        # otherwise, the face is not drawn
        #
        return [
            [p1, p3, p7, p5],  # bottom
            [p1, p5, p6, p2],
            [p5, p7, p8, p6],
            [p7, p3, p4, p8],  # rear
            [p1, p2, p4, p3],  # left
            [p2, p6, p8, p4],
        ]

    # 1. Regular Tetrahedra
    # IN_FILE = 'dipole_180520.res'  # from [volfil_tetrahedron_180519.py] v0.2
    # OUT_FILE = 'cubeGroup_180520_t0950.stl'
    # DIPOLE_SIZE = 5

    # 2. VTK from Gaussian Sphere code
    IN_FILE = 'dipole_180526.res'  # from [volfil_vtkShape_180526.py] v0.1
    # OUT_FILE = 'cubeGroup_180526_t1040.stl'
    # OUT_FILE = 'cubeGroup_180527_t0805.stl'
    OUT_FILE = 'cubeGroup_180527_t1052.stl'
    DIPOLE_SIZE = 0.05

    with open(IN_FILE, 'rb') as rfp:
        dipoles = np.genfromtxt(IN_FILE)

    with open(OUT_FILE, 'wb') as wfp:
        writer = STLWR.Binary_STL_Writer(wfp)

        for adipole in dipoles:
            cube = get_cube(DIPOLE_SIZE, adipole)
            writer.add_faces(cube)

        writer.close()
    print('OUT:', OUT_FILE)

if __name__ == '__main__':
    make_cubeGroup()
