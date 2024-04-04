
emails = []
while True:
    email = input("Enter an email message (press Enter to finish): ")
    if email.strip() == "":
        break
    emails.append(email)

merged_email = "\n\n".join(emails)

print("Merged email:")
print(merged_email)
