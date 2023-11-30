import numpy as np


class Variable:
    def __init__(self, data):
        self.data = data


class Function:
    # def はメソッドの定義
    # 今回は__call__と__forward__の2つのメソッドを定義

    def __call__(self, input):
        x = input.data
        y = self.forward(x) # 具体的な計算はforwardメソッドで行う
        output = Variable(y)
        return output

    # 例外を発生させるメソッド
    def forward(self, x):
        raise NotImplementedError()


# 上で定義したFunctionクラスを継承
class Square(Function):
    def forward(self, x):
        return x ** 2


x = Variable(np.array(10))
f = Square()
y = f(x)
print(type(y))
print(y.data)
