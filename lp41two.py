def main():
  weight = int(input("Please enter weight:"))
  length = int(input("Please enter length:"))
  height = int(input("Please enter height:"))
  width = int(input("Please enter width:"))
  cube = length * height * width
  
  if weight >= 27 and cube >= 100000:
    print("To heavy and to large")
  elif weight >= 27 and cube <= 100000:
    print("To heavy")
  elif weight <=27 and cube >= 100000:
    print("To large")
  else:
    print(" Accepted")
    
  pass


if __name__ == "__main__":
  main()