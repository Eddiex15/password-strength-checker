# password-strength-checker

i created a simple password strength checker using python

here is hgow i builtg it

.import re was added so we could use re.search() to check for patterns like uppercase, lowercase, and numbers.
.password = input("enter your password") grabs the password to test
.then usin if else statement,
First checks length: if len(password)<8
Then checks for uppercase: elif not re.search("[A-Z]", password)
Then lowercase: elif not re.search("[a-z]", password)
Then numbers: elif not re.search("[0-9]", password)

.then gives me a fedback if the password strenght is strong
