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

  def fic(self) -> bool:
    """front is clear"""
    return front_is_clear()


  def fib(self) -> bool:
    """front_is_blocked"""
    return not self.fic()

  def ric(self) -> bool:

    self.tr()
    if self.fic():
      self.tl()
      return True
    self.tl()
    return False 

  def rib(self) -> bool:
    """right is blocked"""
    return not self.ric()
    
  def mazemove(self):
    """maze move"""
    if self.fib():
      self.tl()
    else:
      self.m()
      if self.ric():
        self.tr()
        self.m()
        if self.ric():
          self.tr()
          self.m()
    
    pass

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

  def sweep(self, num):
    for _ in range(num):
      self.pickm(3)
      self.m()
      self.tl()

  def ready(self):
    self.mm(2)
    self.tl()
    self.m()
    self.tr()
  
  


def main():
    """ Karel code goes here! """
    kt=ktools()
    kt.ready()
    kt.sweep(4)
    pass


if __name__ == "__main__":
    run_karel_program()