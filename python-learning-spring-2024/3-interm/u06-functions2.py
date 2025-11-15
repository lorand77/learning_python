def draw_rectangle(h, w, s="o", space_after=True):
    for i in range(h):
        print(s * w)
    if space_after == True:
        print()
    
draw_rectangle(3,5)    
draw_rectangle(3,5,space_after=False)    

draw_rectangle(3,5,"x",False)    
draw_rectangle(h=3,w=5,s="x",space_after=False)   

print("xx","yy")
print("xx","yy",sep=" ",end="\n")
print("xx","yy",sep="---",end="\n\n\n")

draw_rectangle(3,6)    
