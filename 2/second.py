from decimal import  Decimal
from fractions  import Fraction
import decimal
x = Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
print('x = %-5s' %x)
y = Fraction(1,10) + Fraction(1,10) + Fraction(1,10) - Fraction(3,10)
print('y = %-5s' %y)
decimal.getcontext().prec = 2
z = decimal.Decimal(str(1/3)) + decimal.Decimal(str(6/12))
print('z = %-5s' %z)
f = 2.5
F = Fraction(*f.as_integer_ratio())
print(F)

