class Nodo: 
  def __init__(self, valore, cl, cr, parent):
    self.valore = valore
    self.cl = cl
    self.cr = cr
    self.parent = parent

node1 = Nodo(1, 2, 3, None)

print(node1.valore)