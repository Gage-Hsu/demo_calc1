'''
@Author: your name
@Date: 2020-07-03 07:21:28
@LastEditTime: 2020-07-03 07:51:06
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \Vscode_Workspace\demo_calc1\test_calc.py
'''
import unittest
from calc import neuron


class Tests(unittest.TestCase):
    def test_neuron(self):
        self.assertEqual(neuron(1, 2, 3), 5)
        self.assertEqual(neuron(1, -2, 1), 0)
        self.assertEqual(neuron(3, -1, 1), 0)


if __name__ == '__main__':
    unittest.main()
