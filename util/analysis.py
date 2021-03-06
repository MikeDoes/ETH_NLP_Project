import json 

path = 'fin_num_5.json'

with open(path,'r') as f:
    data = json.load(f)

print('Sample Entry', data[0])

unique_paragraph_list = []
for entry in data:
    if entry['paragraph'] not in unique_paragraph_list:
        unique_paragraph_list += [entry['paragraph']]

print('Length of entries', len(data))
print('Length of paragraphs', len(unique_paragraph_list))

category_count = {}
for element in data:
        category = element['category']

        if category not in category_count.keys():
            category_count[category] = 0

        category_count[category] += 1
        print(element)   
print('category count', category_count)

    
    


### Creating a new dataset with the same parahprah as list
new_json = []
for paragraph in unique_paragraph_list:
    entities = []
    for i, entry in reversed(list(enumerate(data))):
        if paragraph == entry['paragraph']:
            del entry['paragraph']
            entities += [entry]
            del data[i]
        entities = entities[::-1]
    new_json += [{'paragraph': paragraph, 'entities':entities}]




#Check that all entities were transferred:
entity_count = 0
for item in new_json:
    entity_count += len(item['entities'])



with open('enron_num.json','w') as f:
    json.dump(new_json, f)


