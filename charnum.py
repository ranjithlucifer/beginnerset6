n=input()
count=0
for i in n:
  if (i.isdigit() or i.isalpha()):
    count+=1
if count!=0:
  print("Yes")
else:
  print("No")
