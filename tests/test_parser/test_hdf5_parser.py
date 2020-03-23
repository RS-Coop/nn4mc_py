import nn4mc_py.parser as nnPr
import unittest

class TestHDF5Parser(unittest.TestCase):

    def setUp(self):
        pass

    def test_basic_1(self):
        p = nnPr.HDF5Parser('Test')

        print('OK')

    def test_file_1(self):
        p = nnPr.HDF5Parser('../data/test_1.hdf5')

        p.parse()

        for node in p.nn.iterate():
            if node.layer.w is not None:
                print(node.layer.identifier)
                print(node.layer.w.values)


if __name__=='__main__':
    unittest.main()
