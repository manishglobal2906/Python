f1=open("Myfile2.txt","w")
f1.write("My Self Manish Kumar Singh \nI am student of Tutedude Classes \nI want to become Python Developer")
f1.close()
print("Reading Line 1:")
try:
  with open("Myfile2.txt","r") as f1:
    x = f1.readline()
    print(x)
    print("Reading Line 2:")
    x = f1.readline()
    print(x)
    print("Reading Line 3:")
    x = f1.readline()
    print(x)
    f1.close()

except FileNotFoundError:
     print("File was not found")
