sports = ["soccer", "basketball", "ping-pong", "swimming", "baseball"]


for v in sports:
    if v[0:3] == "bas":
        print(v)


# for i in range(len(sports)):
#     if sports[i][0:3] == "bas":
#         print(sports[i])


# i = 0
# while i < len(sports):
#     if sports[i][0:3] == "bas":
#         print(sports[i])
#     i = i + 1


print(len(sports))
print(sports[0])     # index 0..L-1
print(sports[-2])    # -1..-L
print(sports[1:4])   # a:b a...b-1      a:b:s (s=step)


hotel_ratings = { "Rat Hole":1, "Five Seasons":5, "Cousin Hotel":2, "Ricotta Hotel":4 }

print(hotel_ratings["Rat Hole"])


for k in hotel_ratings:
    print(k, hotel_ratings[k])


for k,v in hotel_ratings.items():
    print(k, v)


for v in hotel_ratings.values():
    print(v)


a_list = [0,1,2,3,4]
a_dict = {0:0,1:1,2:2,3:3,4:4}   

print(a_list[0])
#a_list[5]   # IndexError: list index out of range
print(a_list[0:3])

print(a_dict[0])
#a_dict[5]   # KeyError
#print(a_dict[0:3]) # CANNOT USE SLICES!!!


a_list[1]=11
print(a_list)

a_dict[1]=11
print(a_dict)

#a_list[100]=11   #IndexError

a_dict[100]=11
print(a_dict)


print(a_list)
del a_list[1]
print(a_list)
print(a_list[1])

print(a_dict)
del a_dict[1]
print(a_dict)
print(a_dict[2])
