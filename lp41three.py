def main():
  eggs = int(input("Please enter number of eggs:"))
  dozens = eggs % 12
  extra = eggs - dozens
  dozen = extra / 12
  price = 0.0
  

  if dozen > 0 and dozen < 4:
    price  = 0.50
  elif dozen > 4 and dozen <6:
    price = 0.45
  elif dozen >6 and dozen <11:
    price = 0.40
  elif dozen >11:
    price = 0.35

  total = price * dozen
  extraprice =
    

  
  
  pass


if __name__ == "__main__":
  main()