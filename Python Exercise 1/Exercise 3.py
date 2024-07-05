def age(brother_1,brother_2):
    if brother_1 > brother_2:
        print('Brother_1 is Elder.')
    else:
        print('Brother_2 is Elder.')

brother_1 = int(input('Age of one brother: '))
brother_2 = int(input('Age of other brother: '))
age(brother_1,brother_2)
