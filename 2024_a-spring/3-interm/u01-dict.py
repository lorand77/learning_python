# # lists

# # grades = [5,3,2]

# # for i in range(len(grades)):
# #     print(grades[i])

# # for v in grades:
# #     print(v)


# subject_likes = {"math":5, "english":5, "history":5, "art history":4, "music":2}

# # () parenthesis
# # [] brackets
# # {} curly brackets

# # print(subject_likes)
# # print(type(subject_likes))

# # print(subject_likes["music"])


# # for k in subject_likes:
# #     print(f"subject:{k} | grade:{subject_likes[k]}")

# # print("*"*20)

# # for k,v in subject_likes.items():
# #     print(f"subject:{k} | grade:{v}")    


# # print(subject_likes.keys())
# # print(subject_likes.values())    

# # for k in subject_likes.keys():
# #     print(f"subject:{k} | grade:{subject_likes[k]}")

# # for v in subject_likes.values():
# #     print(f"grade:{v}")


# print(subject_likes)
# #print(len(subject_likes))

# subject_likes["music"] = 1
# print(subject_likes)

# subject_likes["literature"] = 4
# print(subject_likes)

# print("music" in subject_likes)
# print("PE" in subject_likes)

# subject_likes.pop("music")
# print(subject_likes)


# from sympy.ntheory import factorint

# x = factorint(24, multiple=True)
# print(x)
# print(type(x))

# x = factorint(24)
# print(x)
# print(type(x))


subject_likes = {"math":5, "english":5, "history":5, "art history":4, "music":2}

subject_likes = {"math":5, 
                 "english":5, 
                 "history":5, 
                 "art history":4, 
                 "music":2}

subject_likes = {"math"         : 5, 
                 "english"      : 5, 
                 "history"      : 5, 
                 "art history"  : 4, 
                 "music"        : 2}

subject_likes = {"math"         : 5, 
                 "english"      : 5, 
                 "history"      : 5, 
                 "art history"  : 4, 
                 "music"        : 2
}

subject_likes = {
    "math"         : 5, 
    "literature"   : 4,
    "history"      : 5, 
    "art history"  : 4, 
    "music"        : 2,
    "english"      : 5,
}

print(subject_likes)



a = [1,2,3,4]
a = [
    "loooooooooooong text moooooooooooo",
    "loooooooooooong text moooooooooooo",
    "loooooooooooong text moooooooooooo",
    "loooooooooooong text moooooooooooo",
    "loooooooooooong text moooooooooooo",
    "loooooooooooong text moooooooooooo",
]
print(a)

a = [1,2,3,4,]
print(a)