import re
import json 

path = "fin_num_4.json"
#path = 'fin_num_merged.json'


paragraph_with_non_present_entities = []

with open(path,'r') as f:
    data = json.load(f)

for i, paragraph_dict in enumerate(data):
    for j, entity_dict in enumerate(paragraph_dict['entities']):
        #detected is a variable to check if there is error in the dataset
        detected = False
        target_num = entity_dict['target_num']
        paragraph_text = paragraph_dict['paragraph']
        instances = list(re.finditer(target_num, paragraph_text))
        # Check if offset is missing
        if 'offset_start' not in entity_dict.keys():
            detected = True

        #Check if entity is mismatched
        else:
            offset_start = entity_dict['offset_start']
            offset_end = entity_dict['offset_end']
            entity = paragraph_dict['paragraph'][offset_start:offset_end]

            if entity != entity_dict['target_num']:
                
                detected = True

        if detected:
            if len(instances) == 0:
                paragraph_with_non_present_entities += [i]
                
                continue

            if len(instances) == 1:
                print('Only one instance')
                allocation_index = 0
            

            else:
                print('\nParagraph Text: \n', paragraph_dict['paragraph'])
                print('Troubled Entity: \n', entity_dict)
                for k, instance in enumerate(instances):
                    
                    print(f'Instance #{k}', instance.span())
            
                allocation_index = int(input('\nChosen Instance\n'))
            
            data[i]['entities'][j]['offset_start'], data[i]['entities'][j]['offset_end'] = instances[allocation_index].span()
            
for i in paragraph_with_non_present_entities[::-1]:
    del data[i]
            

with open('enron_fin_num_merged_fixed_offsets.json','w') as f:
    json.dump(data, f)
        

        
