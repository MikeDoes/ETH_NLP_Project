import json
import numpy as np

path = 'fin_num_5.json'


with open(path,'r') as f:
    data = json.load(f)

np.random.seed(42)


train = .7
test = .2
validate = .1

indices = np.random.choice([0, 1, 2], size=len(data), p=[train, test, validate])

train_set, test_set, validate_set = [],[],[]

for i, index in enumerate(indices):
    if index == 0: train_set += [data[i]]
    if index == 1: test_set += [data[i]]
    if index == 2: validate_set += [data[i]]

for dataset, name in zip([train_set, test_set, validate_set], ['train', 'test', 'validate']):

    with open(f'fin_num_5_{name}.json','w') as f:
        json.dump(dataset, f)