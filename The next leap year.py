#leap year python git test
i = 0
year = int(input("Year:"))

y = year

  
while True:
    y = y + 1 
    
    if y % 4 == 0 and y % 100 != 0 and y % 400 != 0:
        break
    
print(f"The next leap year after {year} is {y}") 
 
     


      