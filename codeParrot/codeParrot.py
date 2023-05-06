from transformers import AutoTokenizer, AutoModelWithLMHead, pipeline, AutoModelForCausalLM
  
# tokenizer = AutoTokenizer.from_pretrained("codeparrot/codeparrot")
# model = AutoModelWithLMHead.from_pretrained("codeparrot/codeparrot")

# inputs = tokenizer("def hello_world():", return_tensors="pt")
# outputs = model(**inputs)

# pipe = pipeline("text-generation", model="codeparrot/codeparrot")
# outputs = pipe("def hello_world():")
# print(outputs)

# output2 = pipe("def get_files_size(filename):")
# print(output2)

# output3 = pipe("from transformers import AutoTokenizer, AutoModelForSequenceClassification")
# print(output3)

# checkpoint = "Salesforce/codegen-350M-mono"
# model = AutoModelForCausalLM.from_pretrained(checkpoint)
# tokenizer = AutoTokenizer.from_pretrained(checkpoint)
# text = "def hello_world():"
# completion = model.generate(**tokenizer(text, return_tensors="pt"))
# print(tokenizer.decode(completion[0]))


from transformers import pipeline

pipe = pipeline("text-generation", model="codeparrot/codeparrot")

output1 = pipe("def get_files_size(filename):")
print(output1)
[{'generated_text': 'def get_files_size(filename):\n    try:\n        return os.path.getsize(filename)\n    except OSError:\n        return 0\n\ndef convert_timestamp(timestamp):\n    try:\n        return datetime.datetime.fromtimestamp(timestamp'}]
/////// Correct
import os
import datetime
def get_files_size(filename):
    try:
        return os.path.getsize(filename)
    except OSError:
        return 0
def convert_timestamp(timestamp):
    try:
        return datetime.datetime.fromtimestamp(timestamp)
    except ValueError:
        return None
///////

output2 = pipe("def is_even(value):")
print(output2)
////// Correct
def is_even(value):
    """
    Determine if a given value represents an even number.

    This is not only defined for integers:
    
        >>> is_even(4)
        True
        >>> is_even(3)
        False
        >>> is_even(3.2)
        False

    """
    return value % 2 == 0
//////

output3 = pipe("def is_odd(value):")
print(output3)
////// Correct
def is_odd(value):
    """Returns `true` if `value` is odd (not a `Rational`). Otherwise, returns `false`.
    
    >>> is_odd(1.5)
    True
    >>> is_odd(0)
    False
    """
    return value % 2 != 0
//////

output4 = pipe("def hello_world():")
print(output4)
# incorrect

output5 = pipe("from transformers import AutoTokenizer, AutoModelForSequenceClassification")
print(output5)
//////
Incorrect
//////

output6 = pipe("def is_zero(a):")
print(output6)
////////
Incorrect
///////

output7 = pipe("def get_sum(a, b):")
print(output7)
////////
Incorrect
///////

output8 = pipe("def get_product(a, b):")
print(output8)
////// Correct
def get_product(a, b):
    return a * b
//////