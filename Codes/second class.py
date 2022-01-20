#adding strings
from subprocess import BELOW_NORMAL_PRIORITY_CLASS


y="2"+"2"
print(y)
x="hello" + "charles"
print(x)
#slicing strings
my_string="I am a boy"
print(my_string[3])
print(my_string[2:6])
print(my_string[2:1])
print(my_string[-5])
print(my_string[-9:-5])

#classwork
my_string= "This is 1000 naira"
string2= "This 500 is lovely"
first_value=1000
second_value=500
first_value=int(my_string[8:12])
second_value=int(string2[5:8])
print(first_value+second_value)

#string formatting
my_string= "This is 1000 naira"
string2= "This 500 is lovely"
first_value=int(my_string[8:12])
second_value=int(string2[5:8])
added=(first_value+second_value)
print(f"The sum of {first_value} and  {second_value} is {added}")

#how to use next line and tabs
print("Dear, Buhari. \nPlease don't run for president again\n\tYours in the country\n\tAstroverse Team")

print("""This is a wonderful string



                                Yours in the country.
                                The Astroverse team.""")


#string methods
a="aaboy"
print(a.index("a"))
print(a.rindex("a"))#counts from right
print(a.count("a"))#counts how many times a appears
print(a.replace("a","w"))#replace w with a

#By sentence
My_sentence="Ada is a girl and tunde loves icecream but, ayo does not give him"
a=My_sentence.split(" ")
print(a)

num=['0','4', '3', '2']
otp="".join(num)
print(otp)

#classwork
s1="Ault"
s2="Kelly"
print(s1.replace("lt",s2)+"lt")

#anotherway of solving
#write a program to find all the occurences of "USA" in a given string ignoring the case
str1="Welcome to USA. usa awesome, isn't it?"
sub_string="USA"
temp_str=str1.lower()
count=temp_str.count(sub_string.lower())
print("The USA count is:",count)
#another way fo solving
print("the_usa_count")

#write a program to find the last position of a substracting "Emma in a given string
# given
str1="Emma is a data scientist who knows python, Emma works at google"
print(str1.rindex("Emma"))

str1= "Emma-is-a-data-scientist"
print(str1.replace("-"," "))

# Given
str1="/Jon is @developer & musician"
final_answer=str1.replace("/","").replace("@",""). replace("&","")
print(final_answer)

my_list=("1", "am", "good")
a_list=("she", "is", "a", "queen")
print(my_list + a_list)

x=my_list+a_list
print(x[: :2])#slicing with increament

#Given the list below
list1=[10,20,[300,400, [5000,6000],500],30,40]
#Get 5000 and 500 out of the list and add them together
#Print the result on the terminal
#Keep slicing until there's nothing to slice anymore

print(list1[2][2][0] + list1[2][3])