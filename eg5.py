from multiprocessing import Pool

results = {}
def collect_results(data):
    results[data[0]] = data[1] 

def func(x):
    return (x, x**2)

if __name__ == '__main__':
    p = Pool()
    for i in range(5):
        p.apply_async(func, (i,), callback=collect_results)
    p.close()
    p.join()
    print results
    