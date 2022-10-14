import random

def computer_turn(N):
    if N > 5 and N <= 8:
        return N-5
    elif N > 8:
        return random.randint(1, 3)
    elif N <= 4:
        return N-1
    elif N == 5:
        return random.randint(1, 3)


def get_amount_test(temp,amount):
    temp = int(input())
    while temp < 1 or temp > 3:
        try:
            print('Число не соответствует формату. Попробуйте еще раз:')
            temp = int(input())
        except:
            print('Число не соответствует формату. Попробуйте еще раз:')
            temp = int(input())
    return temp

N = random.randint(3, 40)
temp = 0
print('В кучке', N, 'камня(-ей)')
while N > 1:
    amount = computer_turn(N)
    N -= amount
    print('Компьютер берет', amount, 'камней. В куче осталось',N,'камней')
    if N == 1:
        print('Победа компьютера')
        exit()
    print('Введите, сколько камней вы хотите взять(от 1 до 3): ')
    amount = get_amount_test(temp,amount)
    N -= amount
    print('Вы берете', amount, 'камней. В куче осталось', N, 'камней')
    if N == 1:
        print('Победа игрока')
        exit()