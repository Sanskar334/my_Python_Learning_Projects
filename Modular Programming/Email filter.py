old_email = []
safe_email = []
spam_email = []

email_input = input("\nEnter mails you want to check:\n").lower()
old_email.extend(email for email in email_input.split(","))

# safe_keywords = ["hurry", "urgent", "important", "asap", "immediate", "action required"]

spam_keywords = ["free", "urgent", "limited time", "offer", "sale", "win", "congratulations",
    "click here", "prize", "exclusive", "guarantee", "100% free", "risk-free",
    "trial", "act now", "don't miss", "important", "immediate action",
    "money-back", "bonus", "claim now", "credit card required", "investment",
    "cheapest", "amazing deal"]


important_email = list(filter(lambda x: all(keyword not in x for keyword in spam_keywords), old_email))
safe_email.extend(important_email)
with open("safe_emails.txt", "w") as safe_file:
    for email in important_email:
        safe_file.write(email + "\n")

# spam_email.extend(spam)

spam = list(filter(lambda x: any(keyword in x for keyword in spam_keywords), old_email))
spam_email.extend(spam)
with open("spam_emails.txt", "w") as spam_file:
    for email in spam:
        spam_file.write(email + "\n")

print(spam_email)
print(f"{safe_email}\n")