import json 

path = 'FinNum-3_ConCall_dev.json'

with open(path,'r') as f:
    data = json.load(f)

## to do @satirocoelho tests


print('Sample Entry test', data[0])

unique_paragraph_list = []
for entry in data:
    if entry['paragraph'] not in unique_paragraph_list:
        unique_paragraph_list += [entry['paragraph']]

print('Length of entries', len(data))
print('Length of paragraphs', len(unique_paragraph_list))

### Creating a new dataset with the same parahprah as list
new_json = []
for paragraph in unique_paragraph_list:
    entities = []
    for i, entry in enumerate(data):
        if paragraph == entry['paragraph']:
            del entry['paragraph']
            entities += [entry]
            del data[i]
    new_json += [{'paragraph': paragraph, 'entities':entities}]


with open('fin_num_merged.json','w') as f:
    json.dump(new_json, f)


