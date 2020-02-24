from ._weights import Weight

#Parent class for all available layer types
#NOTE: This is implemented in an abstract class
#manner, but there could be some changes made to make
#this more correct.
class Layer:
    #Input and output data shapes: None if not unspecified
    #TODO!: Compute these properly
    input_shape = [None, None, None]
    output_shape = [None, None, None]
    self.w = None
    self.b = None

    def __init__(self, id, type='unspecified'):
        self.identifier = id #Unique ID
        self.layer_type = type #Layer type (i.e convolution1D)

    #Add weight and bias parameters
    #Takes tuple of (id, values) for weights and biases
    def addParameters(self, weights, bias):
        self.w = Weight(weights[0], weights[1])
        self.b = Weight(bias[0], bias[1])

    def isInput(self): #Defualt behavior is not input
        return False

    def generateInit(): #For derived classes
        pass

    def generateFwd(): #For derived classes
        pass

    def __hash__(self): #Hashes on the identifier
        return hash(self.identifier)

    def __eq__(self, other): #Equality on the unique identifier
        return self.identifier == other.identifier

################################################################################
#Derived classes (i.e specific layer types)

class Conv1D(Layer):
    filters = 0
    kernel_size = []
    strides = []
    padding = ''
    activation = ''
    use_bias = True

    #NOTE: Not sure if this is needed
    #dilation_rate = []

    def generateInit(self):
        init_string = self.identifier + ' = buildConv1D(&' +\
                    self.w.identifier + '[0], ' +\
                    self.b.identifier + ', ' +\
                    str(self.kernel_size[0]) + ', ' +\
                    str(self.strides[0]) + ', ' +\
                    str(self.input_shape[0]) + ', ' +\
                    str(self.input_shape[1]) + ', ' +\
                    str(self.filters) + ', ' +\
                    self.activation + ');\n'

        return init_string

    def generateFwd(self):
        fwd_string = 'data = fwdConv1D(' + self.identifier + ', data);\n'

        return fwd_string

class Conv2D(Layer):
    filters = 0
    kernel_size = []
    strides = []
    padding = ''
    activation = ''
    use_bias = True

    #NOTE: Not sure if these are needed
    #dilation_rate = []
    #data_format = ''

    def generateInit(self):
        init_string = self.identifier + ' = buildConv2D(&' +\
                    self.w.identifier + '[0], ' +\
                    self.b.identifier + ', ' +\
                    str(self.kernel_size[0]) + ', ' +\
                    str(self.kernel_size[1]) + ', ' +\
                    str(self.filters) + ', ' +\
                    str(self.strides[0]) + ', ' +\
                    str(self.strides[1]) + ', ' +\
                    str(self.input_shape[0]) + ', ' +\
                    str(self.input_shape[1]) + ', ' +\
                    str(self.input_shape[2]) + ', ' +\
                    self.activation + ');\n'

    def generateFwd(self):
        fwd_string = 'data = fwdConv2D(' + self.identifier + ', data);\n'

        return fwd_string

class Dense(Layer):
    units = 0
    activation = ''
    use_bias = True
    output_size = 0 #TODO: Fix this, it is wrong

    def generateInit(self):
        init_string = self.identifier + ' = buildDense(&' +\
                    self.w.identifier + '[0], ' +\
                    self.b.identifier + ', ' +\
                    str(self.input_shape[0]) + ', ' +\
                    str(self.output_size) + ', ' +\
                    self.activation + ');\n'

        return init_string

    def generateFwd(self):
        fwd_string = 'data = fwdDense(' + self.identifier + ', data);\n'

        return fwd_string

#NOTE: Not sure about this whole class
#I think some stuff needs to be changed, at least in the templates
class Flatten(Layer):
    def generateInit():
        pass

    def generateFwd():
        pass

class MaxPooling1D(Layer):
    pool_size = []
    strides = []
    padding = ''

    #NOTE: Not sure if these are needed
    #data_format = ''

    def generateInit(self):
        init_string = self.identifier + ' = buildMaxPooling1D(&' +\
                    str(self.pool_size[0]) + ', ' +\
                    str(self.strides[0]) + ', ' +\
                    str(input_shape[0]) + ', ' +\
                    str(input_shape[1]) + ');\n'

        return init_string

    def generateFwd(self):
        fwd_string = 'data = fwdMaxPooling1D(' + self.identifier + ', data);\n'

        return fwd_string

class MaxPooling2D(Layer):
    pool_size = []
    strides = []
    padding = ''

    #NOTE: Not sure if these are needed
    #data_format = ''

    def generateInit(self):
        init_string = self.identifier + ' = buildMaxPooling2D(&' +\
                    str(self.pool_size[0]) + ', ' +\
                    str(self.pool_size[1]) + ', ' +\
                    str(self.strides[0]) + ', ' +\
                    str(input_shape[0]) + ', ' +\
                    str(input_shape[1]) + ', ' +\
                    str(input_shape[2]) + ');\n'

        return init_string

    def generateFwd(self):
        fwd_string = 'data = fwdMaxPooling2D(' + self.identifier + ', data);\n'

        return fwd_string

################################################################################
#TODO: Finish implementing these

class Dropout(Layer):
    def generateInit():
        pass

    def generateFwd():
        pass

class SimpleRNN(Layer):
    units = 0
    activation = ''
    use_bias = True

    def generateInit():
        pass

    def generateFwd():
        pass

class GRU(Layer):
    units = 0
    dropout = 0.0
    recurrent_dropout = 0.0
    activation = ''
    recurrent_activation = ''
    use_bias = True
    go_backwards = True
    stateful = True
    unrool = True
    reset_after = True

    def generateInit():
        pass

    def generateFwd():
        pass

class LSTM(Layer):
    units = 0
    dropout = 0.0
    implementation = 0
    recurrent_dropout = 0.0
    activation = ''
    recurrent_activation = ''
    use_bias = True
    go_backwards = True
    stateful = True
    unrool = True

    def generateInit():
        pass

    def generateFwd():
        pass

class Input(Layer):
    size = 0

    def isInput(self):
        return True

class Activation(Layer):
    activation = ''
