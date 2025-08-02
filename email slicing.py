""""
    Email Slicing

"""

the_name = input('What\'s your name ?').strip().capitalize()
the_email = input ('What\'s your email ?').strip()

the_username = the_email[:the_email.index('@')]
the_website = the_email[the_email.index('@') + 1:]

print(f'Hello {the_name} your email is : {the_email}')
print(f'Your username is : {the_username} \nYour website is : {the_website}')