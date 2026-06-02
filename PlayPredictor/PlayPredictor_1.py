import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

def MarvellousPlayPedictor(data_path):

    # Step 1 : Load data
    data = pd.read_csv(data_path, index_col = 0)

    print("Size of Actual dataset", len(data))

    # Step 2 : Clean, Prepare and Manipulate data
    feature_names = ['Weather', 'Temperature']

    print("Name of Features", feature_names)

    Weather = data.Whether
    Temperature = data.Temperature
    Play = data.Play

    # creating LabelEncoder
    le = preprocessing.LabelEncoder()

    # Converting string labels into numbers.
    Weather_encoded = le.fit_transform(Weather)
    print(Weather_encoded)

    # Converting string labels into numbers.
    Temp_encoded = le.fit_transform(Temperature)
    label = le.fit_transform(Play)

    print(Temp_encoded)

    # Combining Weather and Temperature into single list of tuples
    features = list(zip(Weather_encoded, Temp_encoded))

    # Step 3 : Train Data
    model = KNeighborsClassifier(n_neighbors = 3)

    # Train the model using the training sets
    model.fit(features, label)

    # Step 4 : Test data
    predicted = model.predict([[0,2]]) # 0 : Overcast, 2 : Mild
    print(predicted)

def main():
    print("------------------Jay Shree Krishna------------------")

    print("Machine Learning Application")

    print("Play Predictor application using K Nearest Neighbor algorithm")

    MarvellousPlayPedictor("PlayPredictor.csv")

if __name__ == "__main__":
    main()