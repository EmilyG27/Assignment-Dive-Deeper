# Task 1
Leap_year = int(input("Year: "))

if Leap_year % 4 == 0 and Leap_year % 100 != 0 or Leap_year % 400 == 0:
    print("True")
else:
    print("False")