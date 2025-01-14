from os import listdir
from itertools import cycle
CARD = 1
#color = '#ffb000' # amber
#color = '#33ff33' # green

font='BlockZone'
fontSize='25px'

color = '#ffcc00' # amber apple2
bgcolor = 'black'
theme='punko'

color = 'black'
bgcolor = 'white'
theme = 'vim'

def card_str(x):
  global CARD
  print(f"CARD:{CARD}::{theme}:{bgcolor}:{color}:{color}:{font}:{fontSize}")
  CARD+=1
  print(x)
  print()

def card_middle(title, card):
    n = int((32/2)) - int((len(card)) / 2)
    global CARD
    print(f"CARD:{CARD}::{theme}:{bgcolor}:{color}:{color}:{font}:{fontSize}")
    print(title.center(40))
    CARD+=1
    print('\n' * (n-1), end='')
    for line in card:
        print(line)

    
def binary(f):
    s = []
    for i in range(f, f+30):
        a = i
        b = i + 30
        s.append((f"{a:03} {a:08b}     |     {b:03} {b:08b}").center(40))

    card_middle(f"from: {f} to: {f + 60 - 1}",s)


card_str(f"""{'BINX'.center(40)}

Welcome to BINX game.

A game of using and abusing integers in
programming.

Each card has one of the following
functions:

  AND OR XOR NOT
  INC DEC 
  POPCOUNT 
  SHIFT
  ZERO

Starting from the number 1 the players
have to produce the number 7.

+ each player decides to draw or play

+ if you play, you apply function to the
  previous card's output and compuite
  the new value with your card

+ whoever gets first to the value 7 wins

""")

card_str(f"""{'BINARY'.center(40)}

All the cards in the game take and
return the type uint8_t, which means:
unsigned integer 8 bits (1 byte).

So we have 8 bits to work with
binary   decimal number
0000000  0
0000001  1
0000010  2
0000011  3
0000100  4
0000101  5

The smallest number we can represent is
0, when all the bits are 0, and the
largest one is 255(all 8 bits set to 1).

If we were using uint64_t then we would
have 64 bits(8 bytes) to work with,
smallest number is 0 and the largest is
9223372036854775807 (all 64 bits set to
1).

If you need to work with negative
numbers then you need a signed integer,
int8_t is again 8 bits, but one bit is
used for the sign, if its - or not, so
the smallest number you can have is -128
and the largest is 127.
""")


binary(0)

listed = listdir('./code')
listed = [x for x in listed if x.endswith('.c') and '#' not in x]
starting = cycle(list(listed))

for i in range(CARD+len(listed), 56):
    listed.append(next(starting))
listed.sort()

for fn in listed:
    if '#' in fn:
        continue

    if not '.' in fn:
        continue

    lang = ''
    if fn.endswith('.c'):
        lang = 'c'
    if fn.endswith('.js'):
        lang = "javascript"
    if fn.endswith('.go'):
        lang = "go"
    if fn.endswith('.py'):
        lang = 'python'

    if lang ==  '':
      continue

    print(f"CARD:{CARD}:{lang}:{theme}:{bgcolor}:{color}:{color}:{font}:{fontSize}")
    skip = True
    with open(f"./code/{fn}","r") as f:
        CARD+=1
        card = []
        for line in f.read().splitlines():
            line = line.rstrip()
            line = line.replace("\t","  ")
            card.append(line)

        n = int((32/2)) - int((len(card)) / 2)
        title = f"filename: {fn}"
        print(f"// {title}")          
        print('\n' * (n-1), end='')

        for line in card:
                print(line)
