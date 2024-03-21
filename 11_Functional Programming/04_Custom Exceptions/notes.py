class AnimalValueError(ValueError):
    pass


def produce_animal_sound(animal_type):
    if animal_type == 'DOG':
        print('Woof, woof!')
    elif animal_type == 'Cat':
        print('Meow!')
    else:
        raise AnimalValueError('Incorrect animal type!')
    
produce_animal_sound("DOG")
produce_animal_sound("Cat")
produce_animal_sound("FOX")
