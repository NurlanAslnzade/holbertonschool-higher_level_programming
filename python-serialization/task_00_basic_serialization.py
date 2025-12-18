#!/usr/bin/python3
import json  as j


def serialize_and_save_to_file(filename, data):
    with open(filename, 'w') as f:
        j.dump(data, filename)

def load_and_deserialize(filename):
    with open(filename, 'r') as f:
        data = j.load(f)
        return(data)
