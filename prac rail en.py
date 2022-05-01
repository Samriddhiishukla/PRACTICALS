plaintext=input("ENTER THE PLAIN TEXT: : ")
key=int(input("ENTER THE KEY : "))
text=plaintext.upper()
matrix=[[" " for x in range(len(plaintext))] for y in range(key)]
flag=0
row=0
for i in range(len(text)):
  matrix[row][i]=text[i]
  if row==0:
    flag=0
  elif row==key-1:
    flag=1
  if flag==0:
    row+=1
  else:
    row-=1
for i in range(key):
    "".join(matrix[i])
ciphertext=[]
for i in range(key):
    for j in range(len(text)):
        if matrix[i][j]!=' ':
            ciphertext.append(matrix[i][j])
cipher="".join(ciphertext)
print("THE ENCRYPTED TEXT IS: ",cipher)
        