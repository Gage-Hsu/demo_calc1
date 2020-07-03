'''
@Author: your name
@Date: 2020-07-02 16:04:54
@LastEditTime: 2020-07-03 07:45:37
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \demo_calc1\calc.py
'''


def neuron(x, w, b):
    y = x * w + b
    y = max(0, y)
    return y


if __name__ == "__main__":
    print(f"neuron(4,1,3):{neuron(4,1,3)}")
