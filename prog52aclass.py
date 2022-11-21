class Shape:
  def __init__(self,length,width):
    self.length = length
    self.width = width
    self.area = 0
    self.perim=0
  def calc(self):
    self.area = self.length*self.width
    self.perim = 2* self.length + 2*self.width

  def getarea(self):
    return self.area

  def getperim(self):
    return self.perim

def main():
  length = int(input("input length:"))
  width = int(input("input width:"))
  rectangle = Shape(length,width)
  rectangle.calc()
  area = rectangle.getarea()
  perim = rectangle.getperim()
  print("area",area)
  print("perimiter",perim)
  pass


if __name__ == "__main__":
  main()