from re import split
import re 

# s= 'Here the Regular expression of the python programming..'
# match=re.search(r'python',s)

# print("Start Index :", match.start())
# print("End Index:",match.end())

# p= re.compile('[a-e]')
# print(p.findall("Here the Value of the data.."))

# p=re.compile('\d+')
# print(p.findall("I Went to the Area which one is not give July 3434"))

# RE split():
# print(split('\W+','Words , words , Words'))
# print(split('\W+',"Word's words Words"))
# print(split('\W+',"On 12th Jan 2016, at 11:02 AM"))
# print(split('\D',"On 12th Jan 2016 ,at 12:00 AM"))


# print(re.split('\d+', 'On 12th Jan 2016 , at 11:02 AM', 1))


# print(re.split('\d+','On 12th Jan 2016, at 11:02 AM', 3))

# print(re.split('[a-f]+' , 'Aey man Come here and Watch it',flags=re.IGNORECASE))

# print(re.split('[a-f]+', 'Aey , Boy oh boy , come here  '))


#4. re.sub() :-  its stands for SubString 


# text = "apple is good, apple is sweet"
# result = re.sub("apple", "banana", text)

# print(result)


# text1="apple apple apple banana"
# result1=re.sub("apple","cherry" ,text,count=1)
# print(result1)

# call="phone : 123-456-7890, Alt : 987-654-3210"
# rresult=re.sub(r"\d{3}-\d{3}-\d{4}", "[HIDDEN]", text)
# print(rresult)

# name="Name : John Carter, Age: 30"
# out=re.sub(r"Name: (\w+), Age: (\d+)", r"Age: \2, Name:\1",name)
# print(out)

# text = "Python   is   easy\tto learn.      "
# result = re.subn(r"\s+"," ",text)
# print(result)

# text = " Name : john Carter ,  Age : 45"
# pattren= r"Name: (\w+), Age: (\d+)"
# replacement=r"Age: \2, Name : \1"
# result=re.subn(pattren,replacement, text)
# print(result)


regex = r"([a-zA-z]+) (\d+)"

match = re.search(regex , "I was born on June 24")
if match != None:
    print ("Match at index %s , %s" % (match.start(), match.end()))

    print("FUll match : %s" % (match.group(0)))
    print("Month : %s" % (match.group(1)))
    print("Day : %s" % (match.group(2)))
else:
    print("The regex pattern does not match...")


p= re.compile('\w')
print(p.findall("He said * in some_lang."))

p = re.compile('w+')
print(p.findall("I went to him At 11 A.M.,he \ said *** in some_language."))

p = re.compile('\w')
print(p.findall("he said *** in some_Language... "))


print(split('\W+', 'Words , words Words'))
print(split('W+',"Word's words Words"))
print(split('\W+','On 12th JAn 2016, at 11:02 AM'))
print(split('\d+', 'On 12th Jan 2016, at 11:02 AM'))

regexs=r"[a-zA-Z]+) (\d+)"

match = re.search(regex , "I was born on June 24")
if match != None:
    print("Match at index %s %s" % (match.start(), match.end()))

    print("Month : %s " % (match.group(1)))
    print("Day : %s" % (match.group(2)))
else:
    print("The regex pattern does not match ....")