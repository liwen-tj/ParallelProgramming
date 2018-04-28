# Python多进程编程
# http://www.codexiu.cn/python/blog/939/
## eg1.py
### 创建单个子进程：
from multiprocessing import Process
p = Process(target=run_proc, args=('test',))
创建了一个子进程对象，子进程将会执行run_proc函数体中的代码，args是传入函数体的参数

p.start()
启动子进程，此时子进程和父进程都是系统中的进程

p.join()
当父进程执行到这一行的时候，会等待子进程执行完毕，然后再继续向下执行

## eg2.py
### 启动大量的子进程，可以用进程池的方式批量创建子进程
from multiprocessing import Pool
p = Pool()
### 四种方式 apply apply_async map map_async
### http://xiaoweiliu.cn/2017/07/04/Difference-between-map-apply-map-async-apply-async-Python-multiprocessing-Pool/
p.apply_async(func, args=(i,))

p.close() # 不再继续添加新进程

p.join() # 主进程阻塞，直到所有的子进程全部退出
(如果没有join，主进程一旦执行完，就看不到子进程的打印结果了（不知道是不是强行关闭了子进程）)