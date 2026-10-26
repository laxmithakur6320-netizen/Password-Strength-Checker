print("==============================")
print("   PASSWORD STRENGTH CHECKER  ")
print("==============================")

password = input("enter your password:")

print("password entered succesfully")
print("now we will check its strength.")


has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)

print("contains uppercase:", has_upper)
print("contains lowercase:", has_lower)

has_digit = any(char.isdigit() for char in password)
has_special = any(not char.isalnum() for char in password)

print("contains number:", has_digit)
print("contains special character:", has_special)


has_length = len(password) >= 8 
print("at least 8 characters", has_length)