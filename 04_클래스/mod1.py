def add(a, b) :
    print("현재파일이름 : ", __name__)
    return a + b

def sub(a, b) :
    return a - b


if __name__ == "__main__" :
    print(add(1, 4))
    print(sub(4, 2))