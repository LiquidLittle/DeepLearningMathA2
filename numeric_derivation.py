
def derive(f, x, h=0.0001):
    answer = (f(x+h) - f(x-h)) / (2 * h) 
    return answer
