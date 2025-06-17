#Create a new file.Add the following data in it : hi evry....etc  | do the WAF that replace all occurrences of "java" with "python".

# with open("practice.txt","r") as f:
#  data=f.read()

#  ndata=data.replace("java","python")
# print(ndata)    

# with open("practice.txt","w") as f:
#  f.write(ndata)

word = "learning"
with open("practice.txt","r")as f:
    data=f.read()
    if(data.find(word) != 0):
        print("found")
    else:
        print("not Found") 

def line():
    word="learning"
    data = True 
    line=1
    with open("practice.txt","r") as f:
        while data:
            data =f.readline()
            if(word in data):
                print(line)
                return
            line += 1
    return -1 

line()