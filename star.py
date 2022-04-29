
def listOfOddNumbers(b):
    odds = list(range(1, b, 2))
    return odds


def star(size):
    x = ' '
    base = "***"
    if size / 2 != int(size / 2) and size > 1:
        # print("odd")
        base = '***'
        odd = listOfOddNumbers((size * 2) - 1)
        # print(odd)
        first_base = '{}{}{}'.format(base * size, x * odd[-1], base * size)
        second_base = '{}{}{}'.format(base * size, x * odd[-1], base * size)
        spaces = (len(first_base) / 2)
        # print(spaces)
        if spaces / 2 != int(spaces / 2):
            # print("odd")
            first_head = '{}{}{}'.format(x * (int(spaces)), "*", x)  # the first star
        else:
            first_head = '{}{}{}'.format(x * (int(spaces)), "*", x)  # the first star
        # now lets do the second head

        second_head = ''
        last_head = ''
        second_body_1 = ''
        second_body_2 = ''
        second_space = int(len(first_base) - 2)

        counter = len(odd) - 1
        start = True
        for i in odd:
            if start == True:
                start = False
                front_space = len(first_head) - 3  # to offset the alignment
                last_front_space = len(base * size) - 1  # offset by six
                middle_space = (size ** 2) + 1
            second_head_ = '{}{}{}{}\n'.format(x * front_space, '*', x * (i), '*')
            second_head += second_head_
            last_head_ = '{}{}{}{}\n'.format(x * last_front_space, '*', x * (odd[counter]), '*')
            last_head += last_head_
            front_space -= 1
            last_front_space += 1  # generate front space for the last head of the star

            second_body_1_ = '{}*{}*{}\n'.format(x * i, x * (second_space - (i + i)), x)
            # print(second_space-i)
            second_body_1 += second_body_1_
            second_body_2_ = '{}*{}*{}\n'.format(x * odd[counter], x * (second_space - (odd[counter] + odd[counter])),
                                                 x)
            second_body_2 += second_body_2_
            counter -= 1
        middle_point = '{}*{}*{}'.format(x * (odd[-1] + 2), x * (second_space - ((odd[-1] + 2) * 2)), x)
    elif size > 1:
        # print("even")
        base = '***'
        odd = listOfOddNumbers((size * 2) - 1)
        first_base = '{}{}{}'.format(base * size, x * odd[-1], base * size)
        second_base = '{}{}{}'.format(base * size, x * odd[-1], base * size)
        spaces = (len(first_base) / 2)
        # print(spaces)
        if spaces / 2 != int(spaces / 2):
            print("odd")
            first_head = '{}{}{}'.format(x * (int(spaces)), "*", x)  # the first star
        else:
            first_head = '{}{}{}'.format(x * (int(spaces)), "*", x)  # the first star
        # now lets do the second head

        second_head = ''
        last_head = ''
        second_body_1 = ''
        second_body_2 = ''
        second_space = int(len(first_base) - 2)

        counter = len(odd) - 1
        start = True
        for i in odd:
            if start == True:
                start = False
                front_space = len(first_head) - 3  # to offset the alignment
                last_front_space = len(base * size) - 1  # offset by six
                middle_space = (size ** 2) + 1
            second_head_ = '{}{}{}{}\n'.format(x * front_space, '*', x * (i), '*')
            second_head += second_head_
            last_head_ = '{}{}{}{}\n'.format(x * last_front_space, '*', x * (odd[counter]), '*')
            last_head += last_head_
            front_space -= 1
            last_front_space += 1  # generate front space for the last head of the star

            second_body_1_ = '{}*{}*{}\n'.format(x * i, x * (second_space - (i + i)), x)
            # print(second_space-i)
            second_body_1 += second_body_1_
            second_body_2_ = '{}*{}*{}\n'.format(x * odd[counter], x * (second_space - (odd[counter] + odd[counter])),
                                                 x)
            second_body_2 += second_body_2_
            counter -= 1
    if size > 1:
        middle_point = '{}*{}Believe{}*{}'.format(x * (odd[-1] + 2),
                                                x * int(((second_space - ((odd[-1] + 2) * 2)) / 2) - len('Believe') / 2),
                                                x * int(((second_space - ((odd[-1] + 2) * 2)) / 2) - len('Believe') / 2),
                                                x)
        print(first_head)
        print(second_head.rstrip('\n'))
        print(first_base)
        # print(len(first_base))
        print(second_body_1.rstrip('\n'))
        print(middle_point)
        print(second_body_2.rstrip('\n'))
        print(second_base)
        print(last_head.rstrip('\n'))
        print(first_head)
        # print(list(second_head).reverse())
    elif size == 1:

        first_base = '{}{}{}'.format(base * size, x * 1, base * size)
        second_base = first_base
        spaces = (len(first_base) / 2)
        first_head = '{}{}{}'.format(x * (int(spaces)), "*", x)

        middle_point = '{}*{}*{}'.format(x * 2, x * 1, x)
        print(first_head)
        print(first_base)
        print(middle_point)
        print(second_base)
        print(first_head)

    elif size == 0:
        print('the size must  bigger than 0')


star(3)
