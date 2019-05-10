from _DUMP import me
me.mark('D')
print('Start Prog --Debug Stat \n')

import numpy as np

class prepceptron:
    def __init__(self, number_inputsL, biaseL):
        self.number_inputs = number_inputsL
        self.biase = biaseL
        self.output = 50000
        self.weights = np.random.rand(number_inputsL,1)
        self.threshold = 0
        self.fire = False

    def run(self, inputL = [], *args):
        self.output = 0
        for i in range(self.number_inputs):
            self.output  = self.output + inputL[i] * self.weights[i] + self.biase
            # print(outputL ," --[",self.biase,"] [",self.weights[i],"]")
        # outputL = float(outputL[0])

    def step_Activator(self,threshold):
        self.threshold = threshold
        # outputL = float(outputL)
        if(self.output>=self.threshold):
            self.fire = True
        else:
            self.fire = False

input = [0,1]

neuron = prepceptron(2,0.006)
neuron.run(input)
fire = neuron.step_Activator(0.55)

print("input = ",input)
print("Weights = ",end='')
for i in neuron.weights:
    print(i,end='')
print("\nBias = ",neuron.biase)
print("Using Step function as activator")
print("----------------")
print("Output = ",neuron.output)
print("Statue = ", neuron.fire)



print('\nEnd Prog --Debug Stat')