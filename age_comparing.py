age_1 = int(input("Enter the age of user 1: "))
age_2 = int(input("Enter the age of user 2: "))
age_3 = int(input("Enter the age of user 3: "))

if age_1 > age_2 and age_1 > age_3:
    if age_2 > age_3:
        print("1. User 1\n2. User 2\n3. User 3")
    else:
        print("1. User 1\n2. User 3\n3. User 2")
elif age_2 > age_1 and age_2 > age_3:
    if age_1 > age_3:
        print("1, User 2\n2. User 1\n3. User 3")
    else:
        print("1. User 2\n2. User 3\n3. User 1")
elif age_3 > age_1 and age_3> age_2:
    if age_1 > age_2:
        print("1, User 3\n2. User 1\n3. User 2")
    else:
        print("1. User 3\n2. User 2\n3. User 1")
else:
    print("Ages are equal.")
