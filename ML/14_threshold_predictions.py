def threshold_predictions(probabilities, threshold):
    return [1 if value >= threshold else 0 for value in probabilities]

if __name__ == "__main__":
    print(threshold_predictions([0.2, 0.5, 0.8], 0.5))
