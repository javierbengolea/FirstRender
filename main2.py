import pandas as pd

pb = pd.read_csv('publishers.csv' )  
print(type(pb.to_dict()))