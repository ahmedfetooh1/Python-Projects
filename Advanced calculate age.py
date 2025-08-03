"""
    Calculate age advanced version and training

"""
print('-'*80)
age = int(input('Please write your age :').strip())
unit = input('Choose time unit : Months(m) , Weeks(w) , Days(d) ').strip().lower()

months = age * 12
weeks = months * 4
days = weeks * 7

if unit == 'months' or unit == 'm':
    print(f'You lived for {months:,} Months.')
elif unit == 'weeks'or unit == 'w' :
    print(f'You lived for {weeks:,} Weeks.')
elif unit == 'days' or unit == 'd':
    print(f'You live for {days:,} Days.')
else :
    print('Run agin and write correct age or unit .')

print('-'*80)