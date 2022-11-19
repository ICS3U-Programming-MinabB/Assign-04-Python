#!/usr/bin/env python3
# Created By: Minab Berhane
# Date: November 17 2022
#This program asks the user to enter an integer,n, and a string then it uses a loop to return a larger string

def copy_string():
  # initialize the loop counter and the string copy
  loop_counter = 0
  string_copy = ""

  # get user input as string
  user_string = input("Enter a string: ")
  user_number_string = input("Enter a number: ")
  print("")

  # checks to catch errors
  try:
      # covert user number string to an integer
      user_number_int = int(user_number_string)
      # checks to see if user number string is a whole number
      if (user_number_int > 0):
          # calculate the copies of the user string using the user number string
          for loop_counter in range(user_number_int):
              string_copy = string_copy + user_string 
          print("Original string is : {} ".format(user_string))
          print("New string is : {} ".format(string_copy))
      else:
          print("{} is not a valid input. Please "
                  "enter a positive number.".format(user_number_string))
  except Exception:
      print("{} is not a number. Please try again."
                   .format(user_number_string))
  finally:
    print ("")
    print("Thanks for playing.")

def main():
    # This function calls other functions
    
    # call functions
    copy_string()
    
    
if __name__ == "__main__":
    main()
