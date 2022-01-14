import os 
import json

#Step 1: Loading the annotation
with open('enron json/annotations.json','r') as f:
    annotations = f.read().split('\n')    
    for i, annotation in enumerate(annotations):
        if i == len(annotations)-1: continue
        annotations[i] = json.loads(annotation.encode())

    #annotations = json.load(f)

with open('enron json/categories.json','r') as f:
    categories = f.read().split('\n')    
    for i, category in enumerate(categories):
        if i == len(categories)-1: continue
        categories[i] = json.loads(category.encode())

with open('enron json/documents.json','r') as f:
    documents = f.read().split('\n')    
    for i, document in enumerate(documents):
        if i == len(documents)-1: continue
        documents[i] = json.loads(document.encode())


#Retrieve document by ID
def get_doc_id(documents, id):
    try:
        for document in documents:
            if document['id'] == id:
                return document['content']
    except:
        print(documents)
        print(id)

def get_category_id(documents, id):
    for document in documents:
        if document['id'] == id:
            return document['name']
        

#Step 2: Renaming the categories, ensuring target_num is either integer or float, creating ending offset and adding document
new_annotations = []
for i, annotation in enumerate(annotations):
    if i == len(annotations)-1: continue
    new_annotation = {"claim": 2, }
    new_annotation["paragraph"] = get_doc_id(documents, annotation['document_id'])
    new_annotation["category"] = get_category_id(categories, annotation['category_id'])
    new_annotation["offset_start"] = annotation["first_char"]
    new_annotation["offset_end"] = annotation["first_char"] + annotation["length"]
    new_annotation["target_num"] = new_annotation["paragraph"][new_annotation["offset_start"]:new_annotation["offset_end"]]
    #Is it integer-able?
    try: 
        new_annotation["target_num"] = int(new_annotation["target_num"])
        new_annotations += [new_annotation]
        continue

    except:
        integer_ed = False
    #Is it float-able
    try: 
        new_annotation["target_num"] = float(new_annotation["target_num"])
        new_annotations += [new_annotation]
        continue

    except:
        float_ed = False

print("Number of Annotations", len(new_annotations))
    
with open('enron_original_finnum_schema.json','w') as f:
    json.dump(new_annotations, f)