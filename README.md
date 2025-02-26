# NNDraw

`ndraw` is a Python package that allows users to visualize neural networks easily.

## Installation

Install `NNdraw` using `pip`:

```bash
pip install nndraw
```

## Usage

```python
from nndraw.drawing import draw_neural_network

# Define the neural network structure
parameters = {
    "input_neurons": (20, "lightblue", True),  # 20 input nodes, colored light blue, with labels
    "hidden_layers": [
        (3, "ReLU", "lightgreen", True),  # 3 hidden nodes, ReLU activation, light green, labeled
        (4, "ReLU", False)  # 4 hidden nodes, ReLU activation, default color, no labels
    ],  
    "output_neurons": (2, "Softmax", "red", True),  # 2 output nodes, Softmax activation, red, labeled
    "directed_edges": False  # If False, edges are undirected; if True, edges are directed
}  

# Call the function with unpacked parameters
draw_neural_network(**parameters)
```

### Parameters Explained
`input_neurons` - Tuple `(num_nodes, color, labels)`, defining the number of input neurons, their color, and whether labels are displayed.
`hidden_layers` - List of tuples `(num_nodes, activation, color, labels)`, where each tuple defines a hidden layer.
`output_neurons` - Tuple `(num_nodes, activation, color, labels)`, specifying the number of output neurons, their activation function, color, and labels.
`directed_edges`  - Boolean (`True` or `False`), indicating whether edges between neurons should be directed (arrows) or undirected (lines).

### Notes
- If a color is not provided, the default color (e.g., `"grey"`) is used.
- Activation functions are for visualization purposes only (they are not applied computationally).

## License

This project is licensed under the MIT License.
