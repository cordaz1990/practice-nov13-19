class Atom:
  """ An atom with a number, symbol, and coordinates."""
  def __init__(self, num: init, sym: str, x: float, y:float, z:float) -> None:
      
      """ Create an Atom with number num, string symbol sym, and float coordinates(x,y,z).
      """
      self.number = num
      self.center = (x,y,z)
      self.symbol = sym
      
  def __str__(self) -> str:
      """Return a string representation of this Atom in this format:
        (SYMBOL, X, Y,Z)
      """
      return'({0}, {1}, {2}, {3})'.format(self.symbol, self.center[0], self.center[1], self.center[2])
