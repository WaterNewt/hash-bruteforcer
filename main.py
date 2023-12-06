import hashlib
import sys
import time
import concurrent.futures
import json

def str2md5(input_string):
    md5 = hashlib.md5()
    md5.update(input_string.encode('utf-8'))
    return md5.hexdigest()

def find_password(chunk, target):
    for word in chunk:
        hashed_pass = str2md5(word.strip())
        if target == hashed_pass:
            return word.strip()

def split_wordlist(file_path, num_chunks):
    with open(file_path, "r") as f:
        words = f.readlines()
    chunk_size = len(words) // num_chunks
    return [words[i:i + chunk_size] for i in range(0, len(words), chunk_size)]

if __name__ == "__main__":
    with open('config.json', 'r') as f:
        config = json.load(f)
    threads = config['threads']
    wordlist_file = config['wordlist']
    target = config['target']

    start = time.time()
    with open(wordlist_file, 'r') as f:
        wordlist = f.readlines()

    wordlist_chunks = split_wordlist(wordlist_file, threads)

    with concurrent.futures.ProcessPoolExecutor(max_workers=threads) as executor:
        futures = []
        for chunk in wordlist_chunks:
            future = executor.submit(find_password, chunk, target)
            futures.append(future)

        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                end = time.time()
                duration = end - start
                print(f"Success\nPassword is: {result}")
                print(f"Duration: {str(duration)}")
                sys.exit(0)
