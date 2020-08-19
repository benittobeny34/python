import datetime


def caculate_age(birth_year,birth_month,birth_date):
    current = datetime.datetime.now()
    print(current)
    whole_date = str(current).split(' ',1)[0]
    print(whole_date)
    current_year,current_month,current_date=[int(x) for x in whole_date.split('-')]

    month = [31,28,31,30,31,30,31,31,30,31,30,31];

    if birth_date > current_date:
        current_date = current_date + month[birth_month - 1]
        current_month = current_month  - 1
    if birth_month > current_month :
        current_year = current_year - 1
        current_month = current_month + 12
    date = current_date - birth_date
    mon = current_month - birth_month
    year = current_year - birth_year

    print('Your age is :{} Years {} Month {} Days'.format(year,mon,date))
        


#print(current_year,current_month,current_date)
birth_year = int(input('enter your birth year'))
birth_month = int(input('enter your birth month'))
birth_date = int(input ('enter your birth date'))
caculate_age(birth_year,birth_month,birth_date)



