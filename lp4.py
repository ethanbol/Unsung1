def main():
  eggs = int(input("Please enter number of eggs:"))
  dozen = eggs // 12
  remainder = eggs % 12
  price = 0.0
  price2 = 0.0
  

  if dozen > 0 and dozen < 4:
    price  = 0.50
    price2 = 0.25
  elif dozen > 4 and dozen <6:
    price = 0.45
    price2 = 0.23
  elif dozen >6 and dozen <11:
    price = 0.40
    price2 = 0.20
  elif dozen >11:
    price = 0.35
    price = 0.18
    

  total = price * dozen
  remainder = price2
  cost = total + remainder
  print("Your total is ", cost)
    

  
  
  pass


if __name__ == "__main__":
  main()