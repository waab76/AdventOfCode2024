import hashlib

def main():
    seed = 'bgvyzdsv'
    num = 0
    while True:
        num += 1
        maybe = seed + str(num)
        hash = hashlib.md5(maybe.encode('ascii'))
        if '000000' == hash.hexdigest()[0:6]:
            print(f'The number {num} produces hash {hash.hexdigest()}')
            return
    

if __name__ == '__main__':
    main()