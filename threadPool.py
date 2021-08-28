from concurrent.futures import ThreadPoolExecutor
import time
from check import openChrome

def sayhello(a):
    print("hello: "+ str(a))
    time.sleep(1)

def mutilThread(coreNum, runFunc, userDataList):


    with ThreadPoolExecutor(coreNum) as executor:
        while userDataList:
            each = userDataList.pop()
            print("添加入队列:{}" .format(each))
            executor.submit(runFunc,each)




def main():
    seed=[600,100,150,200]
    
    start1=time.time()
    for each in seed:
        sayhello(each)
    end1=time.time()
    print("time1: "+str(end1-start1))
    start2=time.time()


    with ThreadPoolExecutor(3) as executor:
        while seed:
            ls = [i*60 for i in range(1,len(seed)+1)]

            each = seed.pop(0)
         
            print("renwu ",each)
            executor.submit(openChrome,each)
            if each ==200:
                seed.append(700)
            # time.sleep(1)
            print(seed,ls)


    end2=time.time()
    print("time2: "+str(end2-start2))
    






    start3=time.time()
    with ThreadPoolExecutor(3) as executor1:
        executor1.map(sayhello,seed)
    end3=time.time()
    print("time3: "+str(end3-start3))

if __name__ == '__main__':
    main()