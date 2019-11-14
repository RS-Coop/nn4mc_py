#!/usr/bin/env python

import nn4mp_py
def nnTest():
    nn = nn4mp.NeuralNetwork()

    l0 = nn4mp.Input('Input Layer')
    l1 = nn4mp.Conv1D('Conv1D Layer')
    l2 = nn4mp.Dense('Dense Layer')

    nn.addLayer(l0)
    nn.addLayer(l1)
    nn.addLayer(l2)
    nn.addLayer(l3)

    nn.addEdge(l0,l1)
    nn.addEdge(l1,l2)

    for node in nn.iterate():
        print(node.layer.identifier)


if __name__ == "__main__":
    nnTest()