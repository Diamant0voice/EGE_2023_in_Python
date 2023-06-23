from random import shuffle

jack = 11
queen = 12
king = 14
ace = 15
JOKER = 16
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, king, ace, JOKER] * 4

print('Играем?')
checker = input('Введите y/n: ')
checker = 1 if checker == 'y' or checker == 'Y' or checker == 'н' or checker == 'Н' else 0

print('ну и вали отсюда') if checker != 1 else None
shuffle(deck)
counter = 0

while checker == 1:
    choice = input('Карту берёшь, y/n? ')
    if choice == 'y' or choice == 'Y' or choice == 'н' or choice == 'Н':
        cur_score = deck.pop(); counter += cur_score
        print('ты взял карту достоинством %d.' %cur_score)
        if counter > 21:
            print('ну ты и лох конечно... перебрал!')
            break
        elif counter == 21:
            print('нифига ты чёткий, возьми с полки пирожок!')
            break
        else:
            print('у тебя на руках %d.' %counter)
    else:
        print('ты набрал %d и позорно бежал с корабля...' %counter)
        break

print('Давай, чеши отсюда, нечего тебе тут делать.')      
