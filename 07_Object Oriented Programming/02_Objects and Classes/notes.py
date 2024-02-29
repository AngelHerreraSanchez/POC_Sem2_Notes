# # class User:
# #     def __init__(self):
# #         self.nickname = 'sampleNickname'
# #         self.city = 'sampleCity'

# #     def introduce(self):
# #         print('Hello, I am', self.nickname, 'and I live in', self.city)


# # sample_user = User()
# # sample_user.introduce()
# # print(sample_user.nickname)
# # print(sample_user.city)


# # class User:
# #     def __init__(self, nickname, city):
# #         self.nickname = nickname
# #         self.city = city

# #     def introduce(self):
# #         print('Hello, I am', self.nickname, 'and I live in', self.city)


# # first_user = User('DarkKnight', 'Gotham')
# # second_user = User('Superman', 'Metropolis')
# # third_user = User('Martin', 'Boston')
# # first_user.introduce()
# # second_user.introduce()
# # third_user.introduce()

# class User:
#     def __init__(self, nickname="SampleNickname", city="SampleCity"):
#         self.nickname = nickname
#         self.city = city

#     def introduce(self):
#         print('Hello, I am', self.nickname, 'and I live in', self.city)


# first_user = User('DarkKnight', 'Gotham')
# second_user = User('Superman', 'Metropolis')
# third_user = User('Martin', 'Boston')
# no_name_no_city_user = User()
# no_city_user = User("Fred")
# no_name_user = User(city="Chicago")


# first_user.introduce()
# second_user.introduce()
# third_user.introduce()
# no_name_no_city_user.introduce()
# no_city_user.introduce()
# no_name_user.introduce()

x = 4 
y = 5
z = 3

print(x == y or z)