def transform(input):
    output = {}
    for key, value in input.items():
        for v in value:
            output[v.lower()] = key;
    return output
