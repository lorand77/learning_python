def draw_rectangle(h, w, s):
    for i in range(h):
        print(s * w)
    print()
    
draw_rectangle(3,5,"o")    # positional arguments (same order as in the function def!!!)
draw_rectangle(h=3,w=5,s="o")
draw_rectangle(w=5, h=3,s="o")    # named/keyword arguments (can use any order)



def draw_rectangle(h, w, s="o"):
    for i in range(h):
        print(s * w)
    print()

draw_rectangle(3,5,"x")   
draw_rectangle(3,5)    


def draw_rectangle(h=5, w=10, s="o"):
    for i in range(h):
        print(s * w)
    print()

draw_rectangle(3,5,"x") 
draw_rectangle(3,5) 
draw_rectangle()


def draw_rectangle(h=5, w=10, s="o"):
    for i in range(h):
        print(s * w)
    print()

