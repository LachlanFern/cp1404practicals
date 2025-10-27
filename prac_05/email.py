"""
Emails
Estimate:40 mins
Actual:35 mins
"""

email_to_name = {}
emails= input("Email: ")

while emails != "":
    parts = emails.split("@")[0].split(".")
    name_guess = " ".join([part.capitalize() for part in parts])

    choice = input(f"Is your name {name_guess}? (y/n)").lower()
    if choice =="y" or choice == "":
        name = name_guess
    elif choice == "n" or choice == "no":
        name = input("Name: ")

    else:
        print("please type 'y' or 'n'")

    emails = input("Email: ")

    email_to_name[emails] = name

for email, name in email_to_name.items():
    print(f"{name} ({email})")

