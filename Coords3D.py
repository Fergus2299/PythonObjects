class Coords3D:
    def __init__(self, n1, n2, n3):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

# making a function which takes two Coords3D
# and returns the midpoint

def midpoint(coords1, coords2):
    coord3 = Coords3D((coords1.n1 + coords2.n1)/2,(coords1.n2 + coords2.n2)/2,(coords1.n3 + coords2.n3)/2)
    return (coord3.n1, coord3.n2, coord3.n3)
print(midpoint(Coords3D(9,4,5), Coords3D(4, 3, 12)))
