import json 
import csv

filename = 'data/predictions/test_prediction_RD_15_0.00003_4_finnum_5_bertuncase.csv'
j = 0
predictions = []
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        j += 1
        if j == 1: continue
        
        new_row = []
        new_row += [row[0]]

        new_row += [row[1].replace('[', '').replace(']', '').split(",")]

        for i, i_number in enumerate(new_row[1]):
            try:
                new_row[1][i] = int(i_number)
            except:
                new_row[1][i] = new_row[1][i].replace("'","").replace("'","").replace(" ","") 
        new_row += [row[2].replace('[', '').replace(']', '').split(",")]

        for i, i_number in enumerate(new_row[2]):
            try:
                new_row[2][i] = int(i_number)
            except:
                new_row[2][i] = new_row[2][i].replace("'","").replace("'","").replace(" ","") 
        

        print(new_row)
        predictions += [new_row]

with open('data/predictions/test_prediction_RD_15_0.00003_4_finnum_5_bertuncase.json','w') as f:
    json.dump(predictions, f)
        
