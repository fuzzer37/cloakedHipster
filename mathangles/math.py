a = 3
while a < 1000:
    b = (a-2) * 180
    a = a + 1
    print b
    f = open("out.txt", "w+")
    outp = f.read()
    f.write(outp + `b` + "\n")