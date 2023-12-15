a="Jimmy"
print(a[3])  
print(a[0:3]) # including first and excluding second
# if left blank first will take 0 as input and second will take last character
print(len(a)) 


print(a.strip())  #abhi to hai nahi prr it removes starting and ending spaces
print(a.rstrip("y "))  #abhi to hai nahi prr it removes starting and ending spaces
print(a.lower())  #lowercase the whole
print(a.upper())  #uppercase the whole
print(a.replace('Ji','Ni'))  #replaces the letters, inverted commas mai
print(a.title())        #first letter capital
print(a.swapcase())   #uppercase to lower case and vice versa


num="1,2,3,4,5,6,7,8"
print(num.split(","))   #creates an array of string
print(len(a.center(50)))
print(a.isalnum())      #alphanumeric
print(a.isalpha())      #alphabet
print(a.islower())      #lower
print(a.center(15,'$'))

