import matplotlib.pyplot as plt

def make_scatter_plot_module(x,y):
    """Function to make a scatter plot
    
    Parameters
    ----------
    x : Array
        x values
    y : Array
        y values
    """
    plt.figure()

    # original code 
    plt.scatter(x,y, s = 3)

    #  modified code to demonstrate the use of `importlib`
    # plt.scatter(x,y, s = 3, c = 'red')
    # plt.grid()

    plt.xlabel('X values')
    plt.ylabel('Y values')

    plt.show()