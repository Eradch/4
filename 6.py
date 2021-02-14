from itertools import cycle

print('Программа повторяет элементы списка. Для генерации следющего повторения необходимо нажать Enter, для выхода',
      ' из программы нажмите q')
u_list = input('Введите список, разделяя элементы пробелом: ').split()
iter_ = cycle(u_list)
quit = None

while quit := 'q':
    print(next(iter_), end='')
    quit = input()
    
