

def read_data(data_path, data_type=None):
    with open(data_path, 'r') as f:
        data = f.read().split()
    if data_type:
        return [data_type(x) for x in data]
    return data
