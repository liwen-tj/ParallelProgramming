from multiprocessing import Pool

results = []
def collect_results(data):
    results.append(data)

def func(x):
    return x**2

if __name__ == '__main__':
    p = Pool()
    p.map_async(func, range(5), callback=collect_results)
    p.close()
    p.join()
    print results[0]
    