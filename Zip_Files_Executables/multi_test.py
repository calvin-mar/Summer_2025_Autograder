import multiprocessing as mp
import multiprocessing.spawn

import time
import sys

def loopy():
    start_time = time.time()
    time.sleep(0.01)
    while True:
        time.sleep(0.01)
        print(time.time() - start_time)

def main():
    mp.spawn.freeze_support()
    print("starting")
    p = mp.Process(target=loopy)
    p.start()
    p.join(3)
    if p.is_alive():
        p.kill()
        if p.is_alive():
            print("alive")
            sys.exit()
    print("done")

if __name__ == "__main__":
    main()
    
