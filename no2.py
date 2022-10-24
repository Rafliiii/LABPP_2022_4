
a = input()
b = input()
try:
    with open(f"{a}.txt","r") as zoom:
        files = zoom.readlines()
        n = []
        files[-1] += "/n"
        for x in files :
            n.append(len(x))
            with open(f"{b}.txt","w") as copy:
                for i in files:
                    copy.write(i.rjust(max(n)))
        print(len(x))
    print("berhasil")
except:
    print("tidak berhasil")