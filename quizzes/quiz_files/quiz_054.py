class rainDrops:
    def pour(n:int) -> str:
        out = ''
        d = {3:'i', 5:'a', 7:'o'}
        for k,v in d.items():
            out += (n%k==0)* (f'Pl{v}ng')
        out += (len(out)==0) * str(n)
        return out

test = rainDrops
print(test.pour(n=28))
print(test.pour(n=30))
print(test.pour(n=34))
