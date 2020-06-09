import datetime


class User:
    """ This will help docstring help(User) """

    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday
        name_pic = full_name.split(' ')
        self.first_name = name_pic[0]
        self.last_name = name_pic[-1]

    # user = User('Margarita Matulenko','19960729')
    # print(user.name)
    # print(user.birthday)
    # print(user.first_name)
    # print(user.last_name)

    def age(self):
        """REtrun the age of the user in years"""
        today = datetime.date(2020, 6, 9)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dod = datetime.date(yyyy, mm, dd)
        age_in_days = (today - dod).days
        age_in_years = age_in_days / 365
        return int(age_in_years)


user = User('Margarita Matulenko', '19960729')
print(user.age())
help(User)
