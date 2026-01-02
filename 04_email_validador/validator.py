import re
EMAIL_REGEX = r"^[\w\.-]+@[\w\.-]+\.\w+$"

def validate_email(emails):
    invalid_emails = []
    valid_emails = []
    for email in emails:
        email_clean = email.strip().lower()
        if re.match(EMAIL_REGEX, email_clean):
            valid_emails.append(email)
        else:
            invalid_emails.append(email)
    total = len(emails)

    validation = {
        'valid_emails': valid_emails,
        'invalid_emails': invalid_emails,
        'total': total
    }

    return validation