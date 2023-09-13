size+int(input("enter the size of the dictory (26 for a-z): "))
ascii_dict={}
if size == 26
    alphabet =[chr(ord('a')+i)for i in range(26)]
    ascii_values=[ord(char) for char in alpahbet]
    for i in range(26):
        ascii_dict[alphabet[i]]=ascii_values[i]
    print("Generated Dictionary:",ascii_dict)
else:
    print("invalid size.Please enter 26 for a-z.")