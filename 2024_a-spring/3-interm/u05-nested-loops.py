# print("********************")
# print("********************")
# print("********************")
# print("********************")
# print("********************")
# print()


def draw_rectangle(h, w, s):
    for i in range(h):
        print(s * w)
    print()


def draw_rectangle_with_nested_loops(h, w, s):
    for i in range(h):
        for j in range(w):
            print(s,end="")
        print()
    print()


def draw_rectangle_without_loops(h, w, s):
    print((s * w + "\n") * h)


draw_rectangle(3,5,"o")
draw_rectangle_with_nested_loops(3,5,"x")
draw_rectangle_without_loops(3,5,"o")

exit()
draw_rectangle(3,23,"-")
draw_rectangle(5,32,"+")
draw_rectangle(8,23,".")
draw_rectangle(3,34,"*")
draw_rectangle(6,12,"$")
draw_rectangle(1,15,"#")