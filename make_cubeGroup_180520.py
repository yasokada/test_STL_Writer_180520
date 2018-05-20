import STLWriter as STLWR
# STLWriter
# code from
# http://code.activestate.com/recipes/578246/
# by Manfred Moitzi

'''
v0.1 May, 20, 2018
  - get_cube() takes [size] arg
  - add make_cubeGroup()
'''

def make_cubeGroup():
    def get_cube(size=3):
        # cube corner points
        s = size
        p1 = (0, 0, 0)
        p2 = (0, 0, s)
        p3 = (0, s, 0)
        p4 = (0, s, s)
        p5 = (s, 0, 0)
        p6 = (s, 0, s)
        p7 = (s, s, 0)
        p8 = (s, s, s)

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

    OUT_FILE = 'cubeGroup_180520_t0950.stl'
    with open(OUT_FILE, 'wb') as fp:
        writer = STLWR.Binary_STL_Writer(fp)
        writer.add_faces(get_cube())
        writer.close()
    print('OUT:', OUT_FILE)

if __name__ == '__main__':
    make_cubeGroup()
