#leap year python git test

# the viribale i is used to store data and update after each while loop
i = 0
#this will ask user input then convert the number to string
year = int(input("Year:"))

#used to store the year and add 1
y = year

#while test if it leap year
while True:
    y = y + 1 
    
    if y % 4 == 0 and y % 100 != 0 and y % 400 != 0:
        break
#print out results   
print(f"The next leap year after {year} is {y}") 
 
     


      