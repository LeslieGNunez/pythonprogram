Python 3.13.2 (v3.13.2:4f8bb3947cf, Feb  4 2025, 11:51:10) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #School Bookstore Rewards Program
>>> def Calculate_points ( Books_purchased):
...     if Books_purchased < 2 :
...         return 0
...     elif Books_purchased < 4:
...         return 5
...     elif Books_purchased < 6:
...         return 15
...     elif Books_purchased < 8:
...         return 30
...     else:
...         return 60
... 
...     
>>> def main ():
...     try:
...         books = int(input("Enter the total number of books you purchased this month:"))
...         if books < 0:
...             print("Invalid, input the number of books. Hint: whole number")
...         else:
...             points = Calculate_points(books)
...             print(f"You have {points} reward points.")
...     except ValueError:
...         print("Please input a whole number of books.")
... 
...         
>>> if __name__ == "__main__":
...     main()
