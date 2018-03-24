
def get_envelope(inputSignal):
    # Taking the absolute value

    absoluteSignal = []
    for sample in inputSignal:
        absoluteSignal.append(abs(sample))

    # Peak detection

    intervalLength = 35  # change this number depending on your Signal frequency content and time scale
    outputSignal = []

    for baseIndex in range(0, len(absoluteSignal)):
        maximum = 0
        for lookbackIndex in range(intervalLength):
            maximum = max(absoluteSignal[baseIndex - lookbackIndex], maximum)
        outputSignal.append(maximum)

    return outputSignal