import numpy as np


def main():

    full_board = True

    n = 100
    m = n
    size = 50000
    
    if not full_board:
        xs = np.random.randint(0,n,size=size)
        ys = np.random.randint(0,m,size=size)
        file = f'data/data_{size}_{n}x{m}.txt'
        f = open(file,'w')
        for i in range(size):
            x = xs[i]
            y = ys[i]
            f.write(f'{x} {y}\n')
        f.close()
    else:
        all_pairs = []
        for i in range(n):
            for j in range(m):
                all_pairs.append(f'{i} {j}\n')
                k = i + 900
                l = j + 900
                all_pairs.append(f'{k} {l}\n')
        size = len(all_pairs)
        n += 900
        m += 900
        file = f'data/data_{size}_{n}x{m}.txt'
        f = open(file,'w')
        while len(all_pairs) > 0:
            i = np.random.randint(0,len(all_pairs))
            s = all_pairs.pop(i)
            f.write(s)
        f.close()
    

if __name__ == "__main__":
    main()