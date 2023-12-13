from import1 import Person

if __name__ == '__main__':
    while True:
        print('create new Person')
        firstname    = input('First name: ')
        lastname    = input('Last name: ')
        age     = input('Age : ')
        Person1 = Person(firstname, lastname, age)
        while True:
            selection = '1=first name, 2=last name, 3=full name, 4=age, 5=all items, 6-10=quit: '
            x = input(f'{selection}')
            if x == '1':
                print(Person1.firstname)
            elif x == '2':
                print(Person1.lastname)
            elif x == '3':
                print(Person1.fullname())
            elif x == '4':
                print(Person1.age)
            elif x == '5':
                print("I'am", Person1.fullname(), "and", Person1.age, "old")
            else:
                print('create a new Person?', end=' ')
                break
        stop = input('Y/N? [Y] ')
        if stop.lower() not in ['yes', 'y', '']:
            break