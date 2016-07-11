
def a(i:int) -> list:
    return [i, 2]

if __name__ == '__main__':
    x = a(2)
    x[1] = 10
    b = a(20)
    
    print(x)
    print("hi")
