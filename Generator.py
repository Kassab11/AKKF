from scipy.stats import multivariate_normal
import numpy as np


def Generator(E,Covar, number_particles):
  samples = multivariate_normal.rvs(np.array(E),
                                  Covar,
                                  size=number_particles)
  return samples