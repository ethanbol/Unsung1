from stanfordkarel import *


class ktools:
  def m(self):
    """move"""
    move()
  
  def tl(self):
    """turn left"""
    turn_left()

  def tr(self):
    """turn right"""
    self.tl()
    self.tl()
    self.tl()

  def ta(self):
    """turn around"""
    self.tl()
    self.tl()

  def pick(self):
  """pick beaper"""
    pick_beeper()


  def put(self):
    """put beeper"""
    put_beeper()

  def put2(self):
    self.put()
    self.m()
    self.put()

  def put5(self):
    self.put2()
    self.m()
    self.put2()
    self.m()
    self.put()

  def h(self):
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.m()
    self.m()
    self.tr()
    self.put5()
    self.ta()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.put2()
    self.tl()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.m()
    self.m()
    self.m()

  def e(self):

    self.m()
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.put2()
    self.tr()
    self.m()
    self.m()
    self.tr()
    self.put2()
    self.tl()
    self.m()
    self.m()
    self.tl()
    self.put2()
    self.m()

  def l(self):

    self.m()
    self.tl()
    self.put5()
    self.ta()
    self.m()
    self.m()
    self.m()
    self.m()
    self.tr()
    self.m()
    self.put2()
    self.m()

  def o(self):

    self.m()
    self.m()
    self.put2()
    self.m()
    self.tl()
    self.put5()
    self.tl()
    self.m()
    self.put2()
    self.m()
    self.tl()
    self.put5()
    self.tl()
    self.m()
    self.m()
    self.m()
    self.m()
    
def main():
    """ Karel code goes here! """
    kt=ktools()
    
    pass


if __name__ == "__main__":
    run_karel_program()