""""
    Your age full details

"""

age = int(input('What\'s your Age ?').strip())

months = age * 12
weeks = months * 4
days = weeks * 7
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print('You lived for : ')
print(f'{months} Months.')
print(f'{weeks} Weeks.')
print(f'{days} Days.')
print(f'{hours} Hours.')
print(f'{minutes} Minutes.')
print(f'{seconds} Seconds.')