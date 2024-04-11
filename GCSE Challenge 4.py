criteria1 = False
criteria2 = False

print("""Password criteria:
- Must be at least 8 characters long
- Must contain at least 1 upper case letter and 1 lower case letter
=========================================
Please set a new password: """)


newpassword = str(input())

if len(newpassword) < 8:
    criteria1 = False
else:
    criteria1 = True

if sum(map(str.isupper, newpassword)) and sum(map(str.islower, newpassword)):
        criteria2 = True
else:
        criteria2 = False

if criteria1 == True and criteria2 == True:
    print("Please confirm your new password")
    confirm = str(input())
else:
    print("Criteria not met.")
    quit()

if confirm == newpassword:
    print("Password successfully updated.")
else:
    print("Confirmation does not match new password.")
