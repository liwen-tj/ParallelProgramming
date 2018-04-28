from multiprocessing import Pool

results = {}
def collect_results(data):
    """
    for i in data:
        results[i[0]] = i[1]
    """
    print data
    #global results
    results = data

def func(x):
    return (x, x**2)

if __name__ == '__main__':
    p = Pool()
    p.map_async(func, [0,1,2,3,4], callback=collect_results)
    p.close()
    p.join()
    print results
    