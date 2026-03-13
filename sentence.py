sentence = "Hello, I am learning Python today."

a = sentence.split()
print("split sentence is: ",a)
#print(type(sentence.split()))

for i in a:
    if len(i)>4:
        print(i)

    else:
        print(".")