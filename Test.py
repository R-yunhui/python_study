def hello(msg):
    print(msg)


flag = True

if __name__ == '__main__':
    hello('hello python!')
    flag = False

if flag:
    print("hello true")
else:
    input("按下回车就可以继续运行")

    print("hello false")

x = 1
y = 2
# 换行输出 x y
print(x)
print(y)
print("------")

# 不换行输出 x y
print(x, end=" ")
print(y, end=" ")

