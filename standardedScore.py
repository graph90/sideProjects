def standardedScore(x, μx, yx):
    return (x - μx) / yx
def main():
    x = 0.5
    μx = 0.5
    yx = 0.05
    print("Standardized score: ", standardedScore(x, μx, yx))
main()