import os
import pandas as pd

filename = "data/swbd/Sentence.t2o"

def load_sentence_dict(filename):
    with open(filename) as f:
        d = {}
        for line in f:
            

            d.append(line)
        return d
