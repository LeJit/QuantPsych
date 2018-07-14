from numpy import log, exp, power
def prelecI(p, delta):
    """
    prelecI(p, delta): Prelec Probability Weighing function

    Params:
        p: A vector of probabilities (n x 1)
        delta: A scalar weight
    Output:
        wp: Predicted value of decision weight
    """
    wp = power(exp(-(-log(p))).T, delta)
    return wp
