import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(region,area,bhk):
    try:
        loc_index = __data_columns.index(region.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = bhk
    x[1] = area

    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("Loading saved artifacts...start")
    global __locations
    global __data_columns
    global __model

    with open("./artifacts/columns (1).json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    with open("./artifacts/Mumbai_House_Prices_Model.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("Loading saved artifacts...done")

if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price("Ghansoli", 1259, 3))
    print(get_estimated_price("Panvel", 5000, 8))