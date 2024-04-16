class SampleUtils:
    def __init__(self):
        self.relations = []
        self.weights = []

    def set_relations(self, relations):
        self.relations = relations

    def set_weights(self, weights):
        self.weights = weights

    def get_relations(self):
        return self.relations

    def get_weights(self):
        return self.weights

    def sampling_over_a_chain_join(self):
        _relations = self.get_relations()
        _weights = self.get_weights()
