import numpy as np

def calculate(list):
  if (len(list)<9):
    raise ValueError("List must contain nine numbers.")
  ls=np.array(list).reshape(3,3)
  ret={"mean":[ls.mean(axis=0).tolist(),ls.mean(axis=1).tolist(),np.mean(ls).tolist()],
  "variance":[ls.var(axis=0).tolist(),ls.var(axis=1).tolist(),np.var(ls).tolist()],
  "standard deviation":[ls.std(axis=0).tolist(),ls.std(axis=1).tolist(),np.std(ls).tolist()],
  "max":[ls.max(axis=0).tolist(),ls.max(axis=1).tolist(),np.max(ls).tolist()],
  "min":[ls.min(axis=0).tolist(),ls.min(axis=1).tolist(),np.min(ls).tolist()],
  "sum":[ls.sum(axis=0).tolist(),ls.sum(axis=1).tolist(),np.sum(ls).tolist()],
  }
  
  return ret