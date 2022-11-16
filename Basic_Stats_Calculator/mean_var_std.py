import numpy as np

def calculate(list):

  if len(list) < 9:
    raise ValueError("List must contain nine numbers.")
  
  m = np.reshape(list,(3, 3))
  fd_m = m.flatten()

  calculations = {
    'mean': [m.mean(axis=0).tolist(), m.mean(axis=1).tolist(), fd_m.mean()],
    'variance': [m.var(axis=0).tolist(), m.var(axis=1).tolist(), fd_m.var()],
    'standard deviation': [m.std(axis=0).tolist(), m.std(axis=1).tolist(), fd_m.std()],
    'max': [m.max(axis=0).tolist(), m.max(axis=1).tolist(), fd_m.max()],
    'min': [m.min(axis=0).tolist(), m.min(axis=1).tolist(), fd_m.min()],
    'sum': [m.sum(axis=0).tolist(), m.sum(axis=1).tolist(), fd_m.sum()]
  }
  return calculations