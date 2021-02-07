import matplotlib.pyplot as plt
from collections import Counter


def calc_pi(limit):  # Generator function
    """
    Prints out the digits of PI
    until it reaches the given limit
    """

    q, r, t, k, n, b = 1, 0, 1, 1, 3, 3

    decimal = limit
    counter = 0

    while counter != decimal + 1:
        if 4 * q + r - t < n * t:
            # yield digit
            yield n
            # insert period after first digit
            if counter == 0:
                yield '.'
            # end
            if decimal == counter:
                print('')
                break
            counter += 1
            nr = 10 * (r - n * t)
            n = ((10 * (3 * q + r)) // t) - 10 * n
            q *= 10
            r = nr
        else:
            nr = (2 * q + r) * b
            nn = (q * (7 * k) + 2 + (r * b)) // (t * b)
            q *= k
            t *= b
            b += 2
            k += 1
            n = nn
            r = nr


lim = 300
x = list(calc_pi(lim))
x = x[:1] + x[2:]
data = Counter(x)


for i in range(10):
    plt.bar(i, data[i])
plt.xticks(list(data.keys()))
plt.xlabel('Digits')
plt.ylabel('Count')
plt.title(f'Number of each digit in pi to {lim}dp')
ax = plt.gca()
smallest = min(list(data.values()))
largest = max(list(data.values()))
ax.set_ylim(smallest - (smallest * 0.1), largest + (largest * 0.1))
plt.show()
