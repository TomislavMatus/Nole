import pickle

def load_model(filepath):
    model = pickle.load(open(filepath, 'rb'))
    return model
