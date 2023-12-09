def sampleStandardDeviation(data):
    n = len(data)
    mean = sum(data) / n
    deviations = [(x - mean) ** 2 for x in data]
    variance = sum(deviations) / (n - 1)
    return variance ** 0.5
def main():
    data = [1, 2, 3, 4, 5]
    print(sampleStandardDeviation(data))
main()