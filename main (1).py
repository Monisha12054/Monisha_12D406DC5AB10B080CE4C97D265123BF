def CheckLeap(Year):
  if ((Year % 400 == 0) or (Year % 100 != 0) and (Year % 4 == 0)):
    print("It is a leap Year")
  else:
    print("It is not a leap Year")


Year = int(input("Enter the number: "))
CheckLeap(Year)
