import hashlib
import json

class ChordNodeDescriptor():
    def __init__(self, identifier, process_id):
        self.identifier = identifier
        self.process_id = process_id

def consistent_hash(value, m):
    encoded_value = value.encode('utf-8') # required by hashlib
    hash_val = int(hashlib.sha1(encoded_value).hexdigest(), 16)
    return hash_val % (2 ** m)

def load_data(path, m):
    kv_pairs = []
    with open(path) as dataFile:
        for line in dataFile:
            j = json.loads(line)
            key = consistent_hash(j['name'], m)
            value = j['value']
            kv_pairs.append((key, value))
    return kv_pairs
