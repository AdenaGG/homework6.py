my_dict = {'login': 111111,
           'login2': 22222,
           'login3': 33333}
print(my_dict)

print(my_dict['login'])
my_dict['login'] = 'sssss'
print(my_dict['login'])

my_dict.update({'login1s': '1s1s1s',
                      'login2ss': '2s2s2s'})
del my_dict['login3']
print(my_dict)

my_set = {1, 2, 3, 'one', 'second', 1.5, 1.5, 1, 'one', 2, 'second', True, False, 17}
print(my_set)
my_set.add(21)
my_set.add(24)
my_set.discard(False)
print(my_set)
