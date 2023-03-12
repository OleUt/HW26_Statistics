import scipy.stats
import math

px = 0.9
n = 100
n1 = 95
n2 = 85

# за інтегральною теоремою Лапласа

def f_l(m, n, p):
    x = (m - n * p) / math.sqrt(n * p * (1 - p))
    f = scipy.stats.norm.cdf(x) - 0.5
    return f

f1 = f_l(n1, n, px)
f2 = f_l(n2, n, px)
probability = f1 - f2
print('Integral Laplace theorem:  p =', probability)

