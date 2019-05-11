from _DUMP import me
me.mark('D')
print('Start Prog --Debug Stat \n')

import numpy as np

class prepceptron:
    def __init__(self, number_inputsL, biaseL):
        self.number_inputs = number_inputsL
        self.biase = biaseL
        self.output = 9
        self.weights = np.random.rand(number_inputsL,1)
        self.threshold = 0
        self.fire = False
        self.learning_rate = 0.5
        self.input_train = [
            [0,0],
            [0,1],
            [1,0],
                ]
        self.output_train = [0,1,1]


    def start(self, inputL = [], *args):
        self.output = 0
        for i in range(self.number_inputs):
            self.output  = self.output + inputL[i] * self.weights[i] + self.biase
            # print(outputL ," --[",self.biase,"] [",self.weights[i],"]")

    def step_Activator(self,threshold):
        self.threshold = threshold
        # outputL = float(outputL)
        if(self.output>=self.threshold):
            self.fire = True
        else:
            self.fire = False

    def train(self, input_array,output_train_local):
        output_local = self.start(input_array)
        error = self.output - output_train_local
        print(self.output, output_train_local)

        for i in range(len(self.weights)):
           self.weights[i] =+ error * input_array[i]



neuron = prepceptron(2,0.05)
# neuron.train(0.12)
input_test = [1,1]
print("initial Weights: --")
print("Weights = \t",end='')
for i in neuron.weights:
    print(i,end='')

for i in range(len(neuron.input_train)):
    neuron.train(neuron.input_train[i],neuron.output_train[i])
    print("input = \t",neuron.input_train[i],end='\n\n')
    print("Weights = \t",end='')
    for i in neuron.weights:
        print(i,end='')

neuron.start(input_test)
neuron.step_Activator(0.54)


print("\nUsing Step function as activator\n")

print("input = \t",input_test,end='\n\n')
print("Weights = \t",end='')
for i in neuron.weights:
    print(i,end='')
print("\n\nBias = \t\t",neuron.biase,end='\n\n')
print("")
print("Output = \t",neuron.output,end='\n\n')
print("Statue = \t", neuron.fire,end='\n\n')



print('\nEnd Prog --Debug Stat')