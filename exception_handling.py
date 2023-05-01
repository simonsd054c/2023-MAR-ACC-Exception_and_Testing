# try except block / try catch block / try except else finally block

class NegativeError(Exception):
    pass

# Numerator and denominator from the user and calculate quotient

try:
    n = int(input("Enter a numerator: "))
    d = int(input("Enter a denominator: "))

    # we want to raise an error when either n or d is negative
    if n < 0 or d < 0:
        raise NegativeError("negative number error")

    q = n / d # Exception was thrown/raised on this line for ZeroDivisioError

    print(q)

except ZeroDivisionError as e:
    print(type(e))
    print(e)
    print("Denominator cannot be zero")

except ValueError:
    print("Please type numbers only")

except NegativeError:
    print("No negative numbers please")

except Exception:
    print("Something went wrong!!")

else:
    # whenever try block is successfully executed without raising any exception
    print("I am else block")

finally:
    # this runs at the end no matter if exception was raised or not
    print("I am finally block")



print("The end of the program")




# file handling
# try:
    # open file
    # write something on it - this line may throw error
# except:
    # do something when exception is thrown
# finally:
    # close file