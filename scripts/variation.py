#!/usr/bin/env python3.6
"""Functions for modelling variation in substitution rate."""

class Settings():
    """Class to initialse variables for simulation.
    
    Modify for different simulation conditions."""

    def __init__(self):
        """Initialise variables.
        
        Potential confusion:
        site_alpha is the alpha paramater of the gamma distribution
        used to obtain the site alpha for a gene - Not the alpha of
        the site rates used by evolver.
        similarly site_beta is the beta for the same gamma distribution.
        
        """
        self.gene_alpha = 10
        self.gene_beta = 10
        self.site_alpha = 10
        self.site_beta = 10
        self.lineage_sigma2 = .25
        self.n_bins_per_gene = 10


def modified_tree(tree, multiplier):
    """Modify the branch lengths of a tree.

    Arguements:
    tree - the newick string of a tree with branch lengths
    multiplier - the mean gene rate

    Returns:
    adjusted_tree - tree with modified branch lengths

    """
    import re
    branch_lengths = re.findall(r':[0-9.]+', tree)
    adjusted_tree = tree
    for branch_length in branch_lengths:
        length = branch_length.split(":")[-1]
        adjusted_tree = re.sub(length,
                               str(round(float(length) * multiplier, 7)),
                               adjusted_tree, 1)
    return adjusted_tree

def get_rate(alpha, beta):
    """Draw random number from gamma distribution.
    
    used both for gene rate and site alpha

    Arguements:
    alpha - the shape parameter of the distribution
    beta - the scale parameter of the distribution

    """
    import numpy as np
    return np.random.gamma(alpha, 1/beta)

def relaxed_tree(tree, rate, sigma2):
    """Generate gene tree under relaxed clock.

    Arguments:
    tree - base tree with branch lengths (rate = 1)
    mean - The mean of the normal distribution from which to draw
    log branch rates (average rate for gene)
    sigma2 - The standard deviation of the normal distribution
    from which to draw log branch rates (clock violation)
    
    Returns:
    adjusted_tree - a gene tree that has evolved under a relaxed
    clock

    """

    import re
    import math
    import numpy as np

    branch_lengths = re.findall(r':[0-9.]+', tree)
    adjusted_tree = tree
    for branch_length in branch_lengths:
        length = branch_length.split(":")[-1]
        
        log_rate = np.random.normal(math.log(rate) - sigma2 / 2, sigma2)
        
        adjusted_tree = re.sub(length,
                               str(round(float(length) * math.exp(log_rate), 7)),
                               adjusted_tree, 1)
    return adjusted_tree    
