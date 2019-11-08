import numpy as np
from sklearn.datasets import make_moons
import matplotlib.pyplot as plt
import perceptron as pt
import neural_network as nn


# X = np.array([[-2, 1], [1, 1], [1.5, -0.5], [-2, -1], [-1, -1.5], [2, -2]])
# Y = np.array([[0, 1], [0, 1], [0, 1], [1, 0], [1, 0], [1, 0]])
# b = nn.build_model(X, Y, 500, print_loss=True)

np.random.seed(0)
X, y = make_moons(200, noise=0.20)
print(y)
plt.scatter(X[:, 0], X[:, 1], s=40, c=y, cmap=plt.cm.Spectral)

plt.figure(figsize=(16, 32))
hidden_layer_dimensions = [1, 2, 3, 4]
for i, nn_hdim in enumerate(hidden_layer_dimensions):
    plt.subplot(5, 2, i+1)
    plt.title('HiddenLayerSize%d' % nn_hdim)
    model = nn.build_model(X, y, nn_hdim, print_loss=True)
    #nn.plot_decision_boundary(lambda x: nn.predict(model, x), X, y)

plt.show()