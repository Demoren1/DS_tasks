import sklearn as sk
import pandas as pd
import numpy as np

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)



