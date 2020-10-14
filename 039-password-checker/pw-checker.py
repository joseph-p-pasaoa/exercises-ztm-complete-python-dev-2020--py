def intro_questions():
  global username, password
  print('Please enter your username:')
  username = input()
  print('Password?')
  password = input()

def print_response():
  global username, password
  pw_length = len(password)
  pw_display = '*' * pw_length
  print(f"{username}, your password {pw_display} is {pw_length} characters long.")


username = password = ''
intro_questions()
print_response()
