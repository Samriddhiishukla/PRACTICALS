word=input("ENTER THE CIPHER KEY:")
key=int(input("ENTER THE KEY:"))
nword=""
ascii=nwa=0
for i in word:
    if i.isupper():
        ascii=ord(i)
        nwa=(ascii-key-65)%26+65
    if i.islower():
        ascii=ord(i)
        nwa=(ascii-key-97)%26+97
    nword+=chr(nwa)
print(" THE DECRYPTED TEXT IS:",nword)