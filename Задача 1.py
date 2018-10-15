# coding : utf-8
import sys
#1. Подсчитать, сколько было выделено памяти под переменные в ранее
# разработанных программах в рамках первых трех уроков. Проанализировать
# результат и определить программы с наиболее эффективным использованием памяти.
# Для анализа возьмите любые 1-3 ваших программы. Результаты анализа
# вставьте в виде комментариев к коду.
# P.S. Напишите в комментариях версию Python и разрядность ОС.

# Версия Python 3.7.0, разрдность системы: 64

#def count(num):
num = '15298584518873885698355'
chet = []
nechet = []
for i in num:
    if int(i) % 2 != 0:
        nechet.append(i)
    elif int(i) == 0:
        continue
    else:
        chet.append(i)


    #print(f'Четных {len(chet)}')
    #print(f'Нечетных {len(nechet)}')


def show_size(x, level=0):
    print('\t' * level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for y in x.items():
                show_size(y, level + 1)
        elif not isinstance(x, str):
            for y in x:
                show_size(y, level + 1)
#show_size(num)
# type = <class 'str'>, size = 48, object = 15298584518873885698355

#show_size(chet)
#    type = <class 'list'>, size = 100, object = ['2', '8', '8', '4', '8', '8', '8', '8', '6', '8']
# 	 type = <class 'str'>, size = 26, object = 2
# 	 type = <class 'str'>, size = 26, object = 8
# 	 type = <class 'str'>, size = 26, object = 8
# 	 type = <class 'str'>, size = 26, object = 4
# 	 type = <class 'str'>, size = 26, object = 8
# 	 type = <class 'str'>, size = 26, object = 8
# 	 type = <class 'str'>, size = 26, object = 8
# 	 type = <class 'str'>, size = 26, object = 8
# 	 type = <class 'str'>, size = 26, object = 6
# 	 type = <class 'str'>, size = 26, object = 8

#show_size(nechet)
#    type = <class 'list'>, size = 100, object = ['1', '5', '9', '5', '5', '1', '7', '3', '5', '9', '3', '5', '5']
# 	 type = <class 'str'>, size = 26, object = 1
# 	 type = <class 'str'>, size = 26, object = 5
# 	 type = <class 'str'>, size = 26, object = 9
# 	 type = <class 'str'>, size = 26, object = 5
# 	 type = <class 'str'>, size = 26, object = 5
# 	 type = <class 'str'>, size = 26, object = 1
# 	 type = <class 'str'>, size = 26, object = 7
# 	 type = <class 'str'>, size = 26, object = 3
# 	 type = <class 'str'>, size = 26, object = 5
# 	 type = <class 'str'>, size = 26, object = 9
# 	 type = <class 'str'>, size = 26, object = 3
# 	 type = <class 'str'>, size = 26, object = 5
# 	 type = <class 'str'>, size = 26, object = 5


# 2 урок, задача 5

list = [chr(i) for i in range(32,128)]
key = [f for f in range(32, 128)]
new = dict(zip(key, list))

# show_size(new)

# Вышло многовато

# type = <class 'dict'>, size = 2620, object = {32: ' ', 33: '!', 34: '"', 35: '#', 36: '$', 37: '%', 38: '&', 39: "'", 40: '(', 41: ')', 42: '*', 43: '+', 44: ',', 45: '-', 46: '.', 47: '/', 48: '0', 49: '1', 50: '2', 51: '3', 52: '4', 53: '5', 54: '6', 55: '7', 56: '8', 57: '9', 58: ':', 59: ';', 60: '<', 61: '=', 62: '>', 63: '?', 64: '@', 65: 'A', 66: 'B', 67: 'C', 68: 'D', 69: 'E', 70: 'F', 71: 'G', 72: 'H', 73: 'I', 74: 'J', 75: 'K', 76: 'L', 77: 'M', 78: 'N', 79: 'O', 80: 'P', 81: 'Q', 82: 'R', 83: 'S', 84: 'T', 85: 'U', 86: 'V', 87: 'W', 88: 'X', 89: 'Y', 90: 'Z', 91: '[', 92: '\\', 93: ']', 94: '^', 95: '_', 96: '`', 97: 'a', 98: 'b', 99: 'c', 100: 'd', 101: 'e', 102: 'f', 103: 'g', 104: 'h', 105: 'i', 106: 'j', 107: 'k', 108: 'l', 109: 'm', 110: 'n', 111: 'o', 112: 'p', 113: 'q', 114: 'r', 115: 's', 116: 't', 117: 'u', 118: 'v', 119: 'w', 120: 'x', 121: 'y', 122: 'z', 123: '{', 124: '|', 125: '}', 126: '~', 127: '\x7f'}
# 	 type = <class 'tuple'>, size = 36, object = (32, ' ')
# 		 type = <class 'int'>, size = 14, object = 32
# 		 type = <class 'str'>, size = 26, object =
# 	 type = <class 'tuple'>, size = 36, object = (33, '!')
# 		 type = <class 'int'>, size = 14, object = 33
# 		 type = <class 'str'>, size = 26, object = !
# 	 type = <class 'tuple'>, size = 36, object = (34, '"')
# 		 type = <class 'int'>, size = 14, object = 34
# 		 type = <class 'str'>, size = 26, object = "
# 	 type = <class 'tuple'>, size = 36, object = (35, '#')
# 		 type = <class 'int'>, size = 14, object = 35
# 		 type = <class 'str'>, size = 26, object = #
# 	 type = <class 'tuple'>, size = 36, object = (36, '$')
# 		 type = <class 'int'>, size = 14, object = 36
# 		 type = <class 'str'>, size = 26, object = $
# 	 type = <class 'tuple'>, size = 36, object = (37, '%')
# 		 type = <class 'int'>, size = 14, object = 37
# 		 type = <class 'str'>, size = 26, object = %
# 	 type = <class 'tuple'>, size = 36, object = (38, '&')
# 		 type = <class 'int'>, size = 14, object = 38
# 		 type = <class 'str'>, size = 26, object = &
# 	 type = <class 'tuple'>, size = 36, object = (39, "'")
# 		 type = <class 'int'>, size = 14, object = 39
# 		 type = <class 'str'>, size = 26, object = '
# 	 type = <class 'tuple'>, size = 36, object = (40, '(')
# 		 type = <class 'int'>, size = 14, object = 40
# 		 type = <class 'str'>, size = 26, object = (
# 	 type = <class 'tuple'>, size = 36, object = (41, ')')
# 		 type = <class 'int'>, size = 14, object = 41
# 		 type = <class 'str'>, size = 26, object = )
# 	 type = <class 'tuple'>, size = 36, object = (42, '*')
# 		 type = <class 'int'>, size = 14, object = 42
# 		 type = <class 'str'>, size = 26, object = *
# 	 type = <class 'tuple'>, size = 36, object = (43, '+')
# 		 type = <class 'int'>, size = 14, object = 43
# 		 type = <class 'str'>, size = 26, object = +
# 	 type = <class 'tuple'>, size = 36, object = (44, ',')
# 		 type = <class 'int'>, size = 14, object = 44
# 		 type = <class 'str'>, size = 26, object = ,
# 	 type = <class 'tuple'>, size = 36, object = (45, '-')
# 		 type = <class 'int'>, size = 14, object = 45
# 		 type = <class 'str'>, size = 26, object = -
# 	 type = <class 'tuple'>, size = 36, object = (46, '.')
# 		 type = <class 'int'>, size = 14, object = 46
# 		 type = <class 'str'>, size = 26, object = .
# 	 type = <class 'tuple'>, size = 36, object = (47, '/')
# 		 type = <class 'int'>, size = 14, object = 47
# 		 type = <class 'str'>, size = 26, object = /
# 	 type = <class 'tuple'>, size = 36, object = (48, '0')
# 		 type = <class 'int'>, size = 14, object = 48
# 		 type = <class 'str'>, size = 26, object = 0
# 	 type = <class 'tuple'>, size = 36, object = (49, '1')
# 		 type = <class 'int'>, size = 14, object = 49
# 		 type = <class 'str'>, size = 26, object = 1
# 	 type = <class 'tuple'>, size = 36, object = (50, '2')
# 		 type = <class 'int'>, size = 14, object = 50
# 		 type = <class 'str'>, size = 26, object = 2
# 	 type = <class 'tuple'>, size = 36, object = (51, '3')
# 		 type = <class 'int'>, size = 14, object = 51
# 		 type = <class 'str'>, size = 26, object = 3
# 	 type = <class 'tuple'>, size = 36, object = (52, '4')
# 		 type = <class 'int'>, size = 14, object = 52
# 		 type = <class 'str'>, size = 26, object = 4
# 	 type = <class 'tuple'>, size = 36, object = (53, '5')
# 		 type = <class 'int'>, size = 14, object = 53
# 		 type = <class 'str'>, size = 26, object = 5
# 	 type = <class 'tuple'>, size = 36, object = (54, '6')
# 		 type = <class 'int'>, size = 14, object = 54
# 		 type = <class 'str'>, size = 26, object = 6
# 	 type = <class 'tuple'>, size = 36, object = (55, '7')
# 		 type = <class 'int'>, size = 14, object = 55
# 		 type = <class 'str'>, size = 26, object = 7
# 	 type = <class 'tuple'>, size = 36, object = (56, '8')
# 		 type = <class 'int'>, size = 14, object = 56
# 		 type = <class 'str'>, size = 26, object = 8
# 	 type = <class 'tuple'>, size = 36, object = (57, '9')
# 		 type = <class 'int'>, size = 14, object = 57
# 		 type = <class 'str'>, size = 26, object = 9
# 	 type = <class 'tuple'>, size = 36, object = (58, ':')
# 		 type = <class 'int'>, size = 14, object = 58
# 		 type = <class 'str'>, size = 26, object = :
# 	 type = <class 'tuple'>, size = 36, object = (59, ';')
# 		 type = <class 'int'>, size = 14, object = 59
# 		 type = <class 'str'>, size = 26, object = ;
# 	 type = <class 'tuple'>, size = 36, object = (60, '<')
# 		 type = <class 'int'>, size = 14, object = 60
# 		 type = <class 'str'>, size = 26, object = <
# 	 type = <class 'tuple'>, size = 36, object = (61, '=')
# 		 type = <class 'int'>, size = 14, object = 61
# 		 type = <class 'str'>, size = 26, object = =
# 	 type = <class 'tuple'>, size = 36, object = (62, '>')
# 		 type = <class 'int'>, size = 14, object = 62
# 		 type = <class 'str'>, size = 26, object = >
# 	 type = <class 'tuple'>, size = 36, object = (63, '?')
# 		 type = <class 'int'>, size = 14, object = 63
# 		 type = <class 'str'>, size = 26, object = ?
# 	 type = <class 'tuple'>, size = 36, object = (64, '@')
# 		 type = <class 'int'>, size = 14, object = 64
# 		 type = <class 'str'>, size = 26, object = @
# 	 type = <class 'tuple'>, size = 36, object = (65, 'A')
# 		 type = <class 'int'>, size = 14, object = 65
# 		 type = <class 'str'>, size = 26, object = A
# 	 type = <class 'tuple'>, size = 36, object = (66, 'B')
# 		 type = <class 'int'>, size = 14, object = 66
# 		 type = <class 'str'>, size = 26, object = B
# 	 type = <class 'tuple'>, size = 36, object = (67, 'C')
# 		 type = <class 'int'>, size = 14, object = 67
# 		 type = <class 'str'>, size = 26, object = C
# 	 type = <class 'tuple'>, size = 36, object = (68, 'D')
# 		 type = <class 'int'>, size = 14, object = 68
# 		 type = <class 'str'>, size = 26, object = D
# 	 type = <class 'tuple'>, size = 36, object = (69, 'E')
# 		 type = <class 'int'>, size = 14, object = 69
# 		 type = <class 'str'>, size = 26, object = E
# 	 type = <class 'tuple'>, size = 36, object = (70, 'F')
# 		 type = <class 'int'>, size = 14, object = 70
# 		 type = <class 'str'>, size = 26, object = F
# 	 type = <class 'tuple'>, size = 36, object = (71, 'G')
# 		 type = <class 'int'>, size = 14, object = 71
# 		 type = <class 'str'>, size = 26, object = G
# 	 type = <class 'tuple'>, size = 36, object = (72, 'H')
# 		 type = <class 'int'>, size = 14, object = 72
# 		 type = <class 'str'>, size = 26, object = H
# 	 type = <class 'tuple'>, size = 36, object = (73, 'I')
# 		 type = <class 'int'>, size = 14, object = 73
# 		 type = <class 'str'>, size = 26, object = I
# 	 type = <class 'tuple'>, size = 36, object = (74, 'J')
# 		 type = <class 'int'>, size = 14, object = 74
# 		 type = <class 'str'>, size = 26, object = J
# 	 type = <class 'tuple'>, size = 36, object = (75, 'K')
# 		 type = <class 'int'>, size = 14, object = 75
# 		 type = <class 'str'>, size = 26, object = K
# 	 type = <class 'tuple'>, size = 36, object = (76, 'L')
# 		 type = <class 'int'>, size = 14, object = 76
# 		 type = <class 'str'>, size = 26, object = L
# 	 type = <class 'tuple'>, size = 36, object = (77, 'M')
# 		 type = <class 'int'>, size = 14, object = 77
# 		 type = <class 'str'>, size = 26, object = M
# 	 type = <class 'tuple'>, size = 36, object = (78, 'N')
# 		 type = <class 'int'>, size = 14, object = 78
# 		 type = <class 'str'>, size = 26, object = N
# 	 type = <class 'tuple'>, size = 36, object = (79, 'O')
# 		 type = <class 'int'>, size = 14, object = 79
# 		 type = <class 'str'>, size = 26, object = O
# 	 type = <class 'tuple'>, size = 36, object = (80, 'P')
# 		 type = <class 'int'>, size = 14, object = 80
# 		 type = <class 'str'>, size = 26, object = P
# 	 type = <class 'tuple'>, size = 36, object = (81, 'Q')
# 		 type = <class 'int'>, size = 14, object = 81
# 		 type = <class 'str'>, size = 26, object = Q
# 	 type = <class 'tuple'>, size = 36, object = (82, 'R')
# 		 type = <class 'int'>, size = 14, object = 82
# 		 type = <class 'str'>, size = 26, object = R
# 	 type = <class 'tuple'>, size = 36, object = (83, 'S')
# 		 type = <class 'int'>, size = 14, object = 83
# 		 type = <class 'str'>, size = 26, object = S
# 	 type = <class 'tuple'>, size = 36, object = (84, 'T')
# 		 type = <class 'int'>, size = 14, object = 84
# 		 type = <class 'str'>, size = 26, object = T
# 	 type = <class 'tuple'>, size = 36, object = (85, 'U')
# 		 type = <class 'int'>, size = 14, object = 85
# 		 type = <class 'str'>, size = 26, object = U
# 	 type = <class 'tuple'>, size = 36, object = (86, 'V')
# 		 type = <class 'int'>, size = 14, object = 86
# 		 type = <class 'str'>, size = 26, object = V
# 	 type = <class 'tuple'>, size = 36, object = (87, 'W')
# 		 type = <class 'int'>, size = 14, object = 87
# 		 type = <class 'str'>, size = 26, object = W
# 	 type = <class 'tuple'>, size = 36, object = (88, 'X')
# 		 type = <class 'int'>, size = 14, object = 88
# 		 type = <class 'str'>, size = 26, object = X
# 	 type = <class 'tuple'>, size = 36, object = (89, 'Y')
# 		 type = <class 'int'>, size = 14, object = 89
# 		 type = <class 'str'>, size = 26, object = Y
# 	 type = <class 'tuple'>, size = 36, object = (90, 'Z')
# 		 type = <class 'int'>, size = 14, object = 90
# 		 type = <class 'str'>, size = 26, object = Z
# 	 type = <class 'tuple'>, size = 36, object = (91, '[')
# 		 type = <class 'int'>, size = 14, object = 91
# 		 type = <class 'str'>, size = 26, object = [
# 	 type = <class 'tuple'>, size = 36, object = (92, '\\')
# 		 type = <class 'int'>, size = 14, object = 92
# 		 type = <class 'str'>, size = 26, object = \
# 	 type = <class 'tuple'>, size = 36, object = (93, ']')
# 		 type = <class 'int'>, size = 14, object = 93
# 		 type = <class 'str'>, size = 26, object = ]
# 	 type = <class 'tuple'>, size = 36, object = (94, '^')
# 		 type = <class 'int'>, size = 14, object = 94
# 		 type = <class 'str'>, size = 26, object = ^
# 	 type = <class 'tuple'>, size = 36, object = (95, '_')
# 		 type = <class 'int'>, size = 14, object = 95
# 		 type = <class 'str'>, size = 26, object = _
# 	 type = <class 'tuple'>, size = 36, object = (96, '`')
# 		 type = <class 'int'>, size = 14, object = 96
# 		 type = <class 'str'>, size = 26, object = `
# 	 type = <class 'tuple'>, size = 36, object = (97, 'a')
# 		 type = <class 'int'>, size = 14, object = 97
# 		 type = <class 'str'>, size = 26, object = a
# 	 type = <class 'tuple'>, size = 36, object = (98, 'b')
# 		 type = <class 'int'>, size = 14, object = 98
# 		 type = <class 'str'>, size = 26, object = b
# 	 type = <class 'tuple'>, size = 36, object = (99, 'c')
# 		 type = <class 'int'>, size = 14, object = 99
# 		 type = <class 'str'>, size = 26, object = c
# 	 type = <class 'tuple'>, size = 36, object = (100, 'd')
# 		 type = <class 'int'>, size = 14, object = 100
# 		 type = <class 'str'>, size = 26, object = d
# 	 type = <class 'tuple'>, size = 36, object = (101, 'e')
# 		 type = <class 'int'>, size = 14, object = 101
# 		 type = <class 'str'>, size = 26, object = e
# 	 type = <class 'tuple'>, size = 36, object = (102, 'f')
# 		 type = <class 'int'>, size = 14, object = 102
# 		 type = <class 'str'>, size = 26, object = f
# 	 type = <class 'tuple'>, size = 36, object = (103, 'g')
# 		 type = <class 'int'>, size = 14, object = 103
# 		 type = <class 'str'>, size = 26, object = g
# 	 type = <class 'tuple'>, size = 36, object = (104, 'h')
# 		 type = <class 'int'>, size = 14, object = 104
# 		 type = <class 'str'>, size = 26, object = h
# 	 type = <class 'tuple'>, size = 36, object = (105, 'i')
# 		 type = <class 'int'>, size = 14, object = 105
# 		 type = <class 'str'>, size = 26, object = i
# 	 type = <class 'tuple'>, size = 36, object = (106, 'j')
# 		 type = <class 'int'>, size = 14, object = 106
# 		 type = <class 'str'>, size = 26, object = j
# 	 type = <class 'tuple'>, size = 36, object = (107, 'k')
# 		 type = <class 'int'>, size = 14, object = 107
# 		 type = <class 'str'>, size = 26, object = k
# 	 type = <class 'tuple'>, size = 36, object = (108, 'l')
# 		 type = <class 'int'>, size = 14, object = 108
# 		 type = <class 'str'>, size = 26, object = l
# 	 type = <class 'tuple'>, size = 36, object = (109, 'm')
# 		 type = <class 'int'>, size = 14, object = 109
# 		 type = <class 'str'>, size = 26, object = m
# 	 type = <class 'tuple'>, size = 36, object = (110, 'n')
# 		 type = <class 'int'>, size = 14, object = 110
# 		 type = <class 'str'>, size = 26, object = n
# 	 type = <class 'tuple'>, size = 36, object = (111, 'o')
# 		 type = <class 'int'>, size = 14, object = 111
# 		 type = <class 'str'>, size = 26, object = o
# 	 type = <class 'tuple'>, size = 36, object = (112, 'p')
# 		 type = <class 'int'>, size = 14, object = 112
# 		 type = <class 'str'>, size = 26, object = p
# 	 type = <class 'tuple'>, size = 36, object = (113, 'q')
# 		 type = <class 'int'>, size = 14, object = 113
# 		 type = <class 'str'>, size = 26, object = q
# 	 type = <class 'tuple'>, size = 36, object = (114, 'r')
# 		 type = <class 'int'>, size = 14, object = 114
# 		 type = <class 'str'>, size = 26, object = r
# 	 type = <class 'tuple'>, size = 36, object = (115, 's')
# 		 type = <class 'int'>, size = 14, object = 115
# 		 type = <class 'str'>, size = 26, object = s
# 	 type = <class 'tuple'>, size = 36, object = (116, 't')
# 		 type = <class 'int'>, size = 14, object = 116
# 		 type = <class 'str'>, size = 26, object = t
# 	 type = <class 'tuple'>, size = 36, object = (117, 'u')
# 		 type = <class 'int'>, size = 14, object = 117
# 		 type = <class 'str'>, size = 26, object = u
# 	 type = <class 'tuple'>, size = 36, object = (118, 'v')
# 		 type = <class 'int'>, size = 14, object = 118
# 		 type = <class 'str'>, size = 26, object = v
# 	 type = <class 'tuple'>, size = 36, object = (119, 'w')
# 		 type = <class 'int'>, size = 14, object = 119
# 		 type = <class 'str'>, size = 26, object = w
# 	 type = <class 'tuple'>, size = 36, object = (120, 'x')
# 		 type = <class 'int'>, size = 14, object = 120
# 		 type = <class 'str'>, size = 26, object = x
# 	 type = <class 'tuple'>, size = 36, object = (121, 'y')
# 		 type = <class 'int'>, size = 14, object = 121
# 		 type = <class 'str'>, size = 26, object = y
# 	 type = <class 'tuple'>, size = 36, object = (122, 'z')
# 		 type = <class 'int'>, size = 14, object = 122
# 		 type = <class 'str'>, size = 26, object = z
# 	 type = <class 'tuple'>, size = 36, object = (123, '{')
# 		 type = <class 'int'>, size = 14, object = 123
# 		 type = <class 'str'>, size = 26, object = {
# 	 type = <class 'tuple'>, size = 36, object = (124, '|')
# 		 type = <class 'int'>, size = 14, object = 124
# 		 type = <class 'str'>, size = 26, object = |
# 	 type = <class 'tuple'>, size = 36, object = (125, '}')
# 		 type = <class 'int'>, size = 14, object = 125
# 		 type = <class 'str'>, size = 26, object = }
# 	 type = <class 'tuple'>, size = 36, object = (126, '~')
# 		 type = <class 'int'>, size = 14, object = 126
# 		 type = <class 'str'>, size = 26, object = ~
# 	 type = <class 'tuple'>, size = 36, object = (127, '\x7f')
# 		 type = <class 'int'>, size = 14, object = 127
# 		 type = <class 'str'>, size = 26, object = 