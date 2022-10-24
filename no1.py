a = input()
b = input()

try:
    c = open(f"{a}.txt","r") 
    d = c.read()
    with open(f"{b}.txt","w") as file:
        file.write(d)
        print("berhasil")
except:
    print("tidak berhasil")