string="sai sai kumar"
count=0
s=string.split(" ")
print(s)
for i in range(len(s)):
    if s[i]==s[i+1]:
        count+=1
    else:
        print("error")

print(count)