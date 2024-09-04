from django.shortcuts import render, redirect
import pandas as pd
from .sustain import model
import pickle


# Create your views here.
def handler(request):
    response = None
    if request.method == 'POST':
        genome = request.POST['Name']
        genome_list = list(genome)
        # print(genome_list)
        df_test = pd.DataFrame(genome_list)
        result = predicting(df_test.transpose())
        if result == "Invalid Input":
            return render(request, "index.html", {'response': result})
        if result[0] == 1:
            response = True
        else:
            response = False
    return render(request, "index.html", {'response': response})

def predicting(data):
    # Loading the Neural Network from disk.
    encoder = pickle.load(open("DNASequencing/ecoli-encoder.pickle", 'rb'))
    try:
        data_test = encoder.transform(data).toarray()
        result = model.predict(data_test)
    except:
        return "Invalid Input"
    return result