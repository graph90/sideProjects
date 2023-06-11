# convert array to dataset
import pandas as pd

def convertArrToDataSet(arr):
    dataSet = pd.DataFrame(arr)
    return dataSet
def main():
    arr = [1, 2, 3, 4, 5]
    dataSet = convertArrToDataSet(arr)
    print(dataSet)
main()