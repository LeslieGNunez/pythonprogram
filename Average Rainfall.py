Python 3.13.2 (v3.13.2:4f8bb3947cf, Feb  4 2025, 11:51:10) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Average Rainfall
>>> def average_rainfall():
...     try:
...         years = int(input("Enter the number of years: "))
...         if years < 1:
...             print("The number of years cannot be less than one.")
...             return
...     except ValueError:
...         print("Invalid input. Please enter a whole number for the number of years.")
...         return
... 
...     
>>> total_rainfall = 0.0
>>> total_months = 0
>>> 
>>> for year in range(1, years + 1):
...     print(f"\nYear {year}")
...     for month in range(1, 13):
...         while True:
...             try:
...                 rainfall = float(input(f"  Enter rainfall for month {month} (in inches): "))
...                 if rainfall < 0:
...                     print("Rainfall cannot be negative. Please enter again.")
...                     continue
...                 break
...             except ValueError:
...                 print("Invalid input. Please enter a number.")
...         total_rainfall += rainfall
...         total_months += 1
...         average_rainfall = total_rainfall / total_months
...         print(f"\nTotal months: {total_months}")
...         print(f"Total rainfall: {total_rainfall:.2f} inches")
...         print(f"Average monthly rainfall: {average_rainfall:.2f} inches")
... # Call the function to run it
