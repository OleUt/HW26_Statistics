import matplotlib.pyplot as plt

sample = [10, 13, 10, 9, 9, 12, 12, 6, 7, 9, 8, 9, 11, 9, 14, 13, 9, 8, 8,
          7, 10, 10, 11, 11, 11, 12, 8, 7, 9, 10, 14, 13, 8, 8, 9, 10, 11, 11, 12, 12]

sample.sort()
print('sample =', sample)
n = len(sample)
print('sample size =', n)

# Values
values = list(set(sample))
values.sort()

# Frequencies
frequencies = []
for val in values:
    freq = 0
    for i in sample:
        if i == val:
            freq += 1
    frequencies.append(freq)
relative_frequencies = []
for freq in frequencies:
    relative_frequencies.append(freq / n)

# Frequency distribution
print('Frequency distribution\n\tvalue:', values, '\n\tfrequency:', frequencies,
      '\n\trelative_frequency:', relative_frequencies)

# Function of Empiric distribution F*(x) = nx/n
nx, fx = 0, []
for val in values:
    for r in range(len(values)):
        if values[r] < val:
            nx += frequencies[r]
    fx.append(nx/n)
    nx = 0
print('F*(x) distribution\n\tx:', values, '\n\tF*(x):', fx)

# Moda (polymodal distribution)
max_freq = 0
moda = []
for i in range(len(values)):
    if frequencies[i] > max_freq:
        moda = []
        max_freq = frequencies[i]
        moda.append(values[i])
    else:
        if frequencies[i] == max_freq:
            moda.append(values[i])
print('moda =', moda, 'max_freq =', max_freq)

# Median
if n % 2 != 0:
    median = sample[n//2]
else:
    median = (sample[n//2] + sample[n//2 - 1]) / 2
print('median =',  median)

# Mean
mean = sum(sample) / n
print('mean =', mean)

# Frequency Polygon
v = [values[0]-1]
for val in values:
    v.append(val)
v.append(values[-1] + 1)
f = [0]
for freq in frequencies:
    f.append(freq)
f.append(0)
plt.plot(v, f)
plt.show()

# Histogram
plt.hist(sample, bins=len(values), linewidth=1, edgecolor="white")
plt.show()
