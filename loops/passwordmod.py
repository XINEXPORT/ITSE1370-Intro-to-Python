mypassword = input()
mod_password = ""

modifier = {
    'i': 1,
    'a': '@',
    'm': 'M',
    'B': 8,
    's': '$'
}

for i in mypassword:
    if i in modifier:
        mod_password+= str(modifier[i])
    else:
        mod_password += i
        
mod_password += '!'

print(mod_password)


