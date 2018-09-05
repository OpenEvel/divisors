a = [6,
28,
496,
8128,
33550336,
8589869056,
137438691328,
2305843008139952128,
2658455991569831744654692615953842176,
191561942608236107294793378084303638130997321548169216]

import divisors as dn
import time
f = open('lol', 'w')
try:
    for num in a:
        print('-'*30, file = f)
        start = time.time()
        print(dn.makeDictPrimeDivisors(num), file = f)
        end = time.time() - start
        print('time = ', end, file = f, flush=True)
        print('time = ', end)
finally:
    f.close()