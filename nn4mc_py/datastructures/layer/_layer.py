class Layer:
    def __init__(self, id):
        self.identifier = id
        self.w = []
        self.b = []

    def isInput(self):
        return False

    def __hash__(self):
        return hash(self.identifier)

    def __eq__(self, other):
        return self.identifier == other.identifier

class Conv1D(Layer):
    filters = 0
    kernel_size = []
    strides = []
    padding = ''
    activation = ''
    use_bias = True

class Conv2D(Layer):
    filters = 0
    kernel_size = []
    strides = []
    padding = ''
    activation = ''
    use_bias = True

class Dense(Layer):
    units = 0
    activation = ''
    use_bias = True

class Flatten(Layer):
    pass

class MaxPooling1D(Layer):
    pool_size = []
    strides = []
    padding = ''

class MaxPooling2D(Layer):
    pool_size = []
    strides = []
    padding = ''

class SimpleRNN(Layer):
    units = 0
    activation = ''
    use_bias = True

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

class Input(Layer):
    size = 0

    def isInput(self):
        return True