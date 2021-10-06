def list_demo() :
    my_list = [64, 'hello', 105.7, '', [0,1,2], False]
    print('la. ', my_list[2:4])
    print('1b. ', my_list[4][2])
    my_list[3] = True
    print('1c. ', my_list)
    print('ld. ', my_list[-1])
    my_list.append(True)
    print('le. ', len(my_list))
    print('1f. ', my_list[4:6] + ['2014/11/06', 5])
    my_list.extend('2014/11/06'.split('/'))
    print('lg. ', len(my_list))
    my_list = my_list + [105.7, False, list('abc'), '']
    my_list.remove(105.7)
    print('1h. ', my_list)
    print('li. ', len(my_list))
    print('lj. ', my_list. index (True))
