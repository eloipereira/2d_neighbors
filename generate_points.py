import numpy as np


def main():
    n = 50000
    m = 50000
    size = 50000
    xs = np.random.randint(0,n,size=size)
    ys = np.random.randint(0,m,size=size)
    file = f'data/data_{size}_{n}x{m}.txt'
    f = open(file,'w')
    for i in range(size):
        x = xs[i]
        y = ys[i]
        f.write(f'{x} {y}\n')
    f.close()

if __name__ == "__main__":
    main()