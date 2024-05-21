import numpy as np

def generate_random_data_module(N):
    """Function to generate N random datapoints in the [0,N] interval
    
    Parameters
    ----------
    N : integer
        Number of datapoints to generate (must be positive)
    
    Returns
    -------
    Arrays
        x - with values from [0,N]
        y - with N randomly distributed values
    """
    assert (isinstance(N,int) & (N>0)),'N must be a positive integer'

    x = np.arange(N)
    y = np.random.rand(1,N)

    return x,y

def generate_sine_data_module(N):
    """Function to generate a sine wave in the [0,2pi] interval with
    N datapoints
    
    Parameters
    ----------
    N : integer
        Number of datapoints to generate (must be positive)
    
    Returns
    -------
    Arrays
        x - with N linearly spaced values in the [0,2pi] interval
        y - sine values
    """
    assert (isinstance(N,int) & (N>0)),'N must be a positive integer'

    x = np.linspace(0,2*np.pi,N)
    y = np.sin(x)

    return x,y