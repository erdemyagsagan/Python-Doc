import pandas as pd
import numpy as np

dp = pd.DataFrame(np.random.randint(0,100,9).reshape(3,3),index=["A","B","C"],columns=["Column1","Column2","Column3"])
print(dp)