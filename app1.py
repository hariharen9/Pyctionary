import json 
import difflib 
from difflib import get_close_matches as cm
data = json.load(open("data.json"))

def translate(w):
    if w in data:
        return data[w]
    elif len(cm(w, data.keys())) > 0:
        ans = cm(w, data.keys())[0]
        yn = input(f"Did you mean {ans} instead? Enter Y if yes, or N if no: ").capitalize()
        if yn == "Y":
            return data[cm(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your query." 

    else:
        return "The word doesn't exist. Please double check!"    


word=input("Enter a word: ").lower()
op = translate(word)

if type(op) == list:
    for items in op:
        print(items)
else:
    print(op)        
