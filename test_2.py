from random import *


class Perceptron():
    def __init__(self):

        # И
        self.patterns = [[0, 0],
                         [0, 1],
                         [1, 0],
                         [1, 1]]

        self.answers = [0, 0, 0, 1]

        self.synapsis = [random() + 0.0001 for _ in range(2)]

        self.neurons = [1]

        self.enters = []

    def count_neuron(self):
        self.neurons[0] = 0
        for i, enter in enumerate(self.enters):
            self.neurons[0] += self.synapsis[i] * enter
        self.neurons[0] = 1 if self.neurons[0] > 0.5 else 0

    def study(self):
        g_error = 1
        while g_error > 0:
            g_error = 0
            for i, pattern in enumerate(self.patterns):
                self.enters = pattern
                self.count_neuron()
                l_error = self.answers[i] - self.neurons[0]
                for j, _ in enumerate(self.synapsis):
                    self.synapsis[j] += 0.1 * l_error * self.enters[j]

                g_error += abs(l_error)


def main():
    p = Perceptron()

    p.study()

    for i, pattern in enumerate(p.patterns):
        p.enters = pattern
        p.count_neuron()
        print(p.neurons)


if __name__ == '__main__':
    main()
