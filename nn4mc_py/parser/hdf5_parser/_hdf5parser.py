from nn4mc_py.parser._parser import Parser
from nn4mc_py.datastructures import NeuralNetwork, Layer, Input
from ._layerbuilder import *
import h5py
import numpy as np
import json

# This class deals with parsing an HDF5 file from a keras neural network model.
# It will scrape the file and generate a NeuralNetwork object
# NOTE:
class HDF5Parser(Parser):
    #Maps layer types to code to dynamically build layers
    builder_map = {'Conv1D' : 'Conv1DBuilder()',
                    'Conv2D' : 'Conv2DBuilder()',
                    'Dense' : 'DenseBuilder()',
                    'Flatten' : 'FlattenBuilder()',
                    'MaxPooling1D' : 'MaxPooling1DBuilder()',
                    'MaxPooling2D' : 'MaxPooling2DBuilder()',
                    'Dropout' : 'DropoutBuilder()',
                    'SimpleRNN' : 'SimpleRNNBuilder()',
                    'GRU' : 'GRUBuilder()',
                    'LSTM' : 'LSTMBuilder()',
                    'Input' : 'InputBuilder()',
                    'Activation' : 'ActivationBuilder()'}

    def __init__(self, file_name):
        self.file_name = file_name #HDF5 model file

        self.nn = NeuralNetwork()

    #Parses the model and creates a NeuralNetwork
    #NOTE:
    def parse(self):
        self.parseModelConfig()

        self.parseWeights()

        #self.constructNeuralNetwork()

    #Parses all of the layer metadata
    #NOTE:
    def parseModelConfig(self):
        with h5py.File(self.file_name, 'r') as h5file: #Open file
            configAttr = h5file['/'].attrs['model_config'] #Gets all metadata
            configJSON = self.bytesToJSON(configAttr)

            #This adds an input layer before everything, not sure if it is
            #really neccessary.
            last_layer = Input('input_1','Input')
            self.nn.addLayer(last_layer)

            #NOTE: Could check to see if its sequential here
            for model_layer in configJSON['config']['layers']:
                type = model_layer['class_name']
                name = model_layer['config']['name']
                builder = eval(self.builder_map[type])

                #Build a layer object from metadata
                layer = builder.build_layer(model_layer['config'], name, type)

                self.nn.addLayer(layer) #Add Layer to neural network

                #NOTE: This makes a big assumption that it will always be
                #sequential which it may not !!!!!!!!!!!!!!!!!!!!!!!!!!!
                self.nn.addEdge(last_layer, layer)

                last_layer = layer

    #Parses all of the weights
    #NOTE:
    def parseWeights(self):
        with h5py.File(self.file_name,'r') as h5file: #Open file
            weightGroup = h5file['model_weights'] #Open weight group

            for id in weightGroup.keys():
                try: #Access weights and biases
                    #NOTE: numpy array, hdf5 dataset is similar
                    weight = np.array(weightGroup[id][id]['kernel:0'][()])
                    bias = np.array(weightGroup[id][id]['bias:0'][()])

                    if weight.size > 0 and bias.size > 0:
                        layer = self.nn.getLayer(id)

                        layer.w.addData(weight)
                        layer.b.addData(bias)

                        layer.input_shape = weight.shape
                        layer.output_shape = bias.shape

                except Exception as e: print(e)


    def bytesToJSON(self, byte_array):
        string = byte_array.decode('utf8')
        JSON = json.loads(string)

        return JSON
