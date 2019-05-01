from _ast import mod

import numpy as np


data = np.zeros(4, dtype={'names':('name', 'age', 'waight'),
                          'formats':('U10', 'i4','f8')})


testdata = np.zeros(5, dtype='int32')



rate=26.4
fullUah=5598135
fullUSD=round(fullUah/26.4)
full=fullUSD

per25=full*0.25
left= full-per25
mounses = 50
perMouns = left/mounses

print(full)
print(per25)
print(left)
print(mounses)
print('----')
print(perMouns)
