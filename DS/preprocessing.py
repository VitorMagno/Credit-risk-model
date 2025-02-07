#%%
import pandas as pd
#%%
data = pd.read_csv(filepath_or_buffer="../data/creditcard.csv")
#%%
target = data["Class"]
features = data.columns[:30].to_list()
# %%
data.head()
# %%

