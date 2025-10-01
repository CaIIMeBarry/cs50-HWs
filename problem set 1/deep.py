name = input("what is the answer to the ultimate question of life, the universe, and everything? ").strip().lower()

if name == "42":
    print("Yes")
elif name == "forty-two":  
    print("Yes")
elif name == "forty two":
    print("Yes")
else:
    print("No")
