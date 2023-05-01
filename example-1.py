# We have a list of numbers
# users can add a value or delete a value or access a value
try:
   list_of_numbers = [1, 2, 3]
   print("1. Add to the list")
   print("2. Remove from the list")
   print("3. Access from the list")
   choice = input("Choose your option: ")
   if (choice == "1"):
       number_to_add = int(input("Which number do you want to add? "))
       list_of_numbers.append(number_to_add)
       print(list_of_numbers)
   elif(choice == "2"):
       number_to_remove = int(input("Which number do you want to remove? "))
       list_of_numbers.remove(number_to_remove)
       print(list_of_numbers)
   elif(choice == "3"):
       index_to_access = int(input("Enter the index that you want to access: "))
       print(list_of_numbers[index_to_access])
   else:
       print("Invalid choice")
except ValueError as e:
   if ("invalid literal for int() with base 10:" in str(e)):
       print("Please enter an integer")
   else:
       print("Please enter a value which is in the list")    
except IndexError:
   print("Please enter index within the range")