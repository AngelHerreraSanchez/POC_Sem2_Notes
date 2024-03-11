def empty_strings(user_object):
    for prop_name in user_object.__dict__.keys():
        prop_value = getattr(user_object, prop_name)
        if isinstance(prop_value, str):
            setattr(user_object, prop_name, '')


class Doctor():
    def __init__(self, first_name='John', last_name='Smith'):
        self.first_name = first_name
        self.last_name = last_name
        self.__format_names()

    def __format_names(self):
        self.first_name = self.first_name.title()
        self.last_name = self.last_name.title()

    def introduce(self):
        print('Hi, I am', self.first_name)

    def compare_name(self, name_to_compare):
        if self.first_name == name_to_compare:
            print('We have the same name!')
        else:
            print('Sorry, my name is different...')

    def get_first_last_name_together(self):
        return self.first_name + ' ' + self.last_name


doc_alex = Doctor('Alexander', 'Smith')
doc_alex.introduce()
empty_strings(doc_alex)
doc_alex.introduce()
