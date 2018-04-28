from multiprocessing import Pool

def func(x):
    with open(str(x)+".txt", "w") as f:
        f.write("hello" + str(x))

if __name__ == '__main__':
    p = Pool()
    for i in range(5):
        p.apply_async(func, args=(i,))
    p.close()
    p.join()
    