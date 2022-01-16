import json 

#path = 'fin_num_merged_manual_fix.json'
#path = 'fin_num_merged.json'

#path = 'fin_num_merged_fixed_offsets.json'
path = "fin_num_4.json"

with open(path,'r') as f:
    data = json.load(f)

missing_offsets = 0
mismatched_offsets = 0

for paragraph_dict in data:
    for entity_dict in paragraph_dict['entities']:
        if 'offset_start' not in entity_dict.keys(): 
            print('No offset detected')
            print(paragraph_dict)
            missing_offsets += 1
            continue

        offset_start = entity_dict['offset_start']
        offset_end = entity_dict['offset_end']
        entity = paragraph_dict['paragraph'][offset_start:offset_end]

        if entity != entity_dict['target_num']:
            print('Mismatch detected')
            print(paragraph_dict)
            mismatched_offsets += 1

print('Missing offset count', missing_offsets)
print('Mismatched offset count', mismatched_offsets)

