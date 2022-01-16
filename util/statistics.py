import json 

path = 'fin_num_5.json'

with open(path,'r') as f:
    data = json.load(f)


unique_paragraph_list = []
for entry in data:
    if entry['paragraph'] not in unique_paragraph_list:
        unique_paragraph_list += [entry['paragraph']]

target_num_set = []
for entry in data:
    for entity in entry['entities']:
        target_num_set += [entity] 

print('Length of entries', len(data))
print('Length of paragraphs', len(unique_paragraph_list))
print("Target Num", len(target_num_set))