def get_day(user_info):
    try:
        day = int(input('What is the day of your bday? '))
        user_info.append(day)
    except ValueError:
        print("You entered bad data for the day")
        user_info.append("BAD Day Data")


def get_month(user_info):
    try:
        month = int(input('What is the month (1-12) of your bday? '))
        user_info.append(month)
    except ValueError:
        print("You entered bad data for the month")
        user_info.append("BAD Month Data")

def get_year(user_info):
    try:
        year = int(input('What is the year of your bday? '))
        user_info.append(year)
    except ValueError:
        print("You entered bad data for the year")
        user_info.append("BAD Year Data")


def get_user_bday(user_info):
    get_day(user_info)
    get_month(user_info)
    get_year(user_info)
    print('So your bday is', user_info)


print('Hi, I will collect some info about your bday!')
user_info = []
get_user_bday(user_info)
