h=5
for i in range(1, h + 1):
    for j in range(h - i,0,-1):
        print "",
    for j in range(1, i*2):
        print "*",
    print "\n"
    
