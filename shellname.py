ti=input("enter the shell name")
if ti=='bash':
    p_filename='/etc/bashrc'
elif ti=='ksh':
    p_filename='/etc/kshrc'
elif ti=='csh' or ti=='tchs':
    p_filename='/etc/cshrc'
else:
    ti="/etc/profile"
    p_filename='/bin/nologin'

print("Shell Name:",ti,"Profile name:",p_filename)