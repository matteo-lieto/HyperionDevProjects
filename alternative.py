#Part 1 alternate char

#Alternate cases in String
# initializing string
my_string = "Andy don't chew on that!"

# printing original string
print("The original string is : " + str(my_string))


#empty list
alt_string = ""

#block code
# Using upper() + lower() + loop

for i in range(len(my_string)):
	if i % 2:
		alt_string = alt_string + my_string[i].upper()
	else:
		alt_string = alt_string + my_string[i].lower()

# printing result
print("The alternate case string is : " + str(alt_string))

#part2 alternate words

my_string_2 = "Andy don't chew on that!"


#block code to split the sentence
my_string_split_2 = my_string_2.split()   


#Empty list to store a to be split list of words, 

string_sep =""

#block code to make every alternate word

for i in range(0, len(my_string_split_2)): #loop to make every second letter upper

    if i % 2 == 0:
        string_sep = string_sep + " "+ my_string_split_2[i].lower() 

    else:
        string_sep = string_sep +" " + my_string_split_2[i].upper() 
    

#Block code to join the individual characters
alt_my_string_2 = "".join(string_sep)

#Block code to product the final results
print("The alternate capilized word case string is : " + alt_my_string_2)


