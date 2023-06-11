import numpy as np
def convertArrToNPArr(arr):
    npArr = np.array(arr)
    return npArr
def main():
    arr = [1, 2, 3, 4, 5]
    npArr = convertArrToNPArr(arr)
    print(npArr)
main()