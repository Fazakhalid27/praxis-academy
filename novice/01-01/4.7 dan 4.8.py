'''def validate(hand):
    if hand < 0 or hand > 2:
        return False
    return True

def print_hand(hand, name='Tamu'):
    hands = ['Batu', 'Kertas', 'Gunting']
    print(name + ' memilih: ' + hands[hand])

def judge(player, computer):
    if player == computer:
        return 'Seri'
    elif player == 0 and computer == 1:
        return 'Kalah'
    elif player == 1 and computer == 2:
        return 'Kalah'    
    elif player == 2 and computer == 0:
        return 'Kalah'
    else:
        return 'Menang'
print('Memulai permainan Batu Kertas Gunting!')

player_name = input('Masukkan nama Anda: ')

print('Pilih tangan: (0: Batu, 1: Kertas, 2: Gunting)')
player_hand = int(input('Masukkan nomor (0-2): '))

if validate(player_hand):
    computer_hand = 1
    
    print_hand(player_hand, player_name)
    print_hand(computer_hand, 'Komputer')

    result = judge(player_hand, computer_hand)
    print('Hasil: ' + result)
else:
    print('Mohon masukkan nomor yang benar')'''

'''def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

print(ask_ok('Do you really want to quit?'))'''

'''def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

print(cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch"))'''



def make_incrementor(n):
    return lambda x: x + n
f = make_incrementor(42)
print(f(2))

def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

print(f('spam'))