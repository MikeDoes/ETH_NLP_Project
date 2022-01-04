# ETH_NLP_Project

Repository with datasets  and model  for number-entity recognition task.
--to be continued

### Dataset

The dataset is composed of 409 different paragraphs with 1191 annotations. The categories are 'other', 'relative', 'date', 'quantity_absolute', 'money', 'change', 'quantity_relative', 'absolute', 'product_number'.

### Models
We are developing two different models for this task.

The fisrt approach treats named entitity recognition as a text-2-text task . 
Given a paragraph where a number "x" of category "cathegory_1" appears , we train the model to output " x : cathegory_1 -".
This implemenation is based on fine-tuning  T5 , check "T5_NLP.ipynb"
