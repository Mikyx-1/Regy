from regy.registry import Registry
@Registry.register(category="models", name="LinearModel")
class LinearModel:
    def __init__(self, input_dim, output_dim):
        self.input_dim = input_dim
        self.output_dim = output_dim

    def __repr__(self):
        return f"LinearModel({self.input_dim} -> {self.output_dim})"