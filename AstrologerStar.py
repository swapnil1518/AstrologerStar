#pattern print
#taken an input integer
#boolean true or false
#if true print normal if flase print reverse star

print("print pattern")
num = int(input("Enter no of rows: "))
print("Enter 1 or 0 ")
bool_val = input("1 for normal and 0 for reverse pattern: ")
if bool_val == "1":
    for i in range(0,num+1):
        print("*" *int(i))
if bool_val == "0":
    for i in range(num,0,-1):
        print("*" *int(i))