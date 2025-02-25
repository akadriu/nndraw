# ndraw

nndraw is a Python package that allows users to draw neural networks easily.

## Installation

```bash
pip install nndraw
```

## Usage

```python
from ndraw.drawing import draw_neural_network

parameters = {
    "input_neurons": (20, "lightblue", True), 
    "hidden_layers": [
        (3, "Linear", "lightgreen", True), #three nodes, node color is lightgreen, labels for nodes
        (4, "ReLU", False) #four nodes, no color specified for nodes, no labels for nodes
    ],  
    "output_neurons": (2, "Softmax", "red", True), 
    "directed_edges": False #edges are undirected
}  

# Call the function with unpacked parameters
draw_neural_network(**parameters)
```

## License

This project is licensed under the MIT License.