# WAP to accept a users First and Last name and print them in
# reverse order with spaces

fn = input("Input First Name- ")
ln = input("Input Last Name- ")

rev_fn = fn[::-1]
rev_ln = ln[::-1]

for i in range(len(rev_ln)):
    print(rev_ln[i],end=" "),

for i in range(len(rev_fn)):
    print(rev_fn[i],end=" "),  
