# To Binary Conversion

def cheating(n:int):
    return bin(n)[2:]

def to_bin(n: int):
    output = ""
    while n > 1:
        output += str(n % 2)
        n = n // 2
    output += str(n)
    return output


print(cheating(9))
print(to_bin(9))
