"""
CP1404 Practical
Emails
Estimate: 20 minutes
Actual:   22 minutes
"""
email_to_name = {}
email = input("Email: ")
while email != "":
    email_and_name_pair = email.split("@")  # change variable name
    is_name = input(f"Is your name {email_and_name_pair[0]}? (Y/n) ").upper()
    if is_name == "Y":
        email_to_name[email] = email_and_name_pair[0]
    else:
        name_of_email = input("Name: ")
        email_to_name[email] = name_of_email
    email = input("Email: ")

for email, name in email_to_name.items():
    print(f"{name} ({email})")
