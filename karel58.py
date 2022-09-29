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

  def sob(self)-> bool:
    return beepers_present()

  def jump(self):
    """jump for 510"""
    while self.fic():
      self.m()
    self.tl()
    while self.rib():
      self.m()
    self.tr()
    self.m()
    self.tr()
    while self.fic():
      self.m()
    self.tl()

  def find(self):
    """find 515"""
    while not facing_north():
      self.tl()
    self.m()
    if not self.sob():
      self.tl()
      self.m()
      self.tl()
      self.m()
    for _ in range(2):
      if not self.sob():
        self.m()
        self.tl()
        self.m()
    pass
    
    
    
  


def main():
    """ Karel code goes here! """
    kt=ktools()
    kt.mm(4)
    kt.tl()
    kt.mm(4)
    kt.tr()
    while not kt.sob():
      kt.put()
      kt.fic()
      kt.m()
      kt.tl()
      kt.fib()
      if kt.fib():
        kt.tr()  
      if not kt.fic():
        kt.tr()
    pass


if __name__ == "__main__":
    run_karel_program()