import re

email = input()

def is_valid_email_format(email):

  pattern = r"^[A-Za-z0-9]*[A-Za-z][A-Za-z0-9]*@[A-Za-z]+\.[A-Za-z]+$"
  if re.match(pattern, email):
    return True
  else:
    return False


if is_valid_email_format(email):
    print('OK')
else:
    print('WRONG')
