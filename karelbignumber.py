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
  
  def mm(self, num):
    for number in range(num):
      self.m()


  def pickm(self, num):
    for i in range(num-1):
      self.pick()
      self.m()
    self.pick()


  def putm(self, num):
    for _ in range(num-1):
      self.put()
      self.m()
    self.put()


  def one(self, num):
    for _ in range(num):
      self.m()
      self.tl()
      self.mm(5)
      self.ta()
      self.putm(5)
      self.tl()
      self.m()


  def zero(self, num):
    for _ in range(num):
      self.m()
      self.tl()
      self.putm(5)
      self.tr()
      self.m()
      self.put()
      self.m()
      self.tr()
      self.putm(5)
      self.tr()
      self.m()
      self.put()
      self.ta()
      self.m()
      self.m()

    
def main():
    """ Karel code goes here! """
    kt=ktools()
    kt.one(1)
    kt.zero(15)
    
    pass


if __name__ == "__main__":
    run_karel_program()