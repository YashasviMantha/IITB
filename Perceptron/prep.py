from _DUMP import me
me.mark('D')
print('Start Prog --Debug Stat')

import numpy as np

class prepceptron:
    def __init__(self, number_inputsL, biaseL):
        self.number_inputs = number_inputsL
        self.biase = biaseL

        self.weights = np.random.rand(number_inputsL,1)

    def run(self, inputL = [], *args):
        outputL = 0
        for i in range(self.number_inputs):
            outputL  = outputL + (inputL[i] * self.weights[i] + self.biase)

        return outputL

input = [0,1]

neuron = prepceptron(2,0.006)

output = neuron.run(input)

print(output)






print('End Prog --Debug Stat')