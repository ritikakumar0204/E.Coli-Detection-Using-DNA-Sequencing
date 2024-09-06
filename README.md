# E.Coli-Detection-Using-DNA-Sequencing

### Overview

This project focuses on detecting E. coli virus using DNA sequencing techniques. The dataset consists of a small portion of DNA encoded into four types of molecules: Adenine (A), Cytosine (C), Guanine (G), and Thymine (T). The goal is to analyze DNA sequences and identify patterns or mutations that indicate the presence of E. coli virus. This project involves Multi Layer Perceptron (MLP) Classifier model. This model is based on Neural Net-Architecture and provides very high peformance with less training time. 

A web-based application built with Django is deployed on an AWS EC2 instance for users to input DNA sequences and get predictions.

### Dataset 

Dataset link: https://archive.ics.uci.edu/ml/machine-learning-databases/molecular-biology/promoter-gene-sequences/promoters.data

The dataset is hosted on the UCI Machine Learning Repository and contains promoter gene sequences for the DNA analysis. Each row in the dataset consists of a binary class label indicating if the sequence is a promoter (positive) or non-promoter (negative), followed by the 57 nucleotide sequence.

Each line in the dataset follows this format:

- `class`: + for promoter and - for non-promoter
- `id` : DNA Sequence id
- `sequence`: 57 characters consisting of A, C, G, and T

### Model Features
The model used in this project is a Multi-Layer Perceptron (MLP) classifier, which is a feedforward artificial neural network. The MLP classifier is trained on the promoter sequences to classify DNA sequences as either promoter regions (positive) or non-promoter regions (negative).

Key features of the MLP model:

Input layer: 57 nodes (one for each nucleotide in the sequence)
Hidden layers: Configurable with the number of nodes and layers optimized through experimentation
Output layer: Binary classification (promoter vs. non-promoter)

Training and testing are performed on a split dataset, and performance metrics such as accuracy, precision, recall, and F1-score are used to evaluate the model.

### Deployment

A Django web application is developed to allow users to upload DNA sequences and receive predictions from the trained MLP classifier. The app is deployed on an AWS EC2 instance for accessibility.

App Features:
- Upload DNA Sequences: Users can input a valid DNA sequences (A, C, G, T) and get predictions on whether the sequence contains promoter regions.
- View Prediction Results: The app returns a positive or negative prediction
- Model Integration: The MLP model is integrated into the app to perform real-time predictions.

![image](https://github.com/user-attachments/assets/ba181765-026b-4e0e-b9f9-78e7bff19c06)


  

  


