class User:
    def __init__(self):
        self.nickname = 'sampleNickname'
        self.city = 'sampleCity'

    def introduce(self):
        print('Hello, I am', self.nickname, 'and I live in', self.city)


sample_user = User()
sample_user.introduce()
print(sample_user.nickname)
print(sample_user.city)


class User:
    def __init__(self, nickname, city):
        self.nickname = nickname
        self.city = city

    def introduce(self):
        print('Hello, I am', self.nickname, 'and I live in', self.city)


first_user = User('DarkKnight', 'Hell')
second_user = User('Ruler_of_Darkness', 'Darkness')
third_user = User('Martin', 'Boston')


first_user.introduce()
second_user.introduce()
third_user.introduce()
