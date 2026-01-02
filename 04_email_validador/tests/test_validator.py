from validator import validate_email

def test_email_valid():
    emails = ['icaro@gmail.com']
    result = validate_email(emails)
    
    assert result['valid_emails'] == ['icaro@gmail.com']
    assert result['invalid_emails'] == []
    assert result['total'] == 1

def test_email_invalid():
    emails = ['icaro@gmail.com', 'emailinvalido']
    result = validate_email(emails)

    assert result['valid_emails'] == ['icaro@gmail.com']
    assert result['invalid_emails'] == ['emailinvalido']
    assert result['total'] == 2
