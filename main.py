
import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp

# load data
heart = pd.read_csv('heart_disease.csv')
yes_hd = heart[heart.heart_disease == 'presence']
no_hd = heart[heart.heart_disease == 'absence']

chol_hd = yes_hd.chol
print(np.mean(chol_hd))

tstat, pval = ttest_1samp(chol_hd, 240)
print(pval/2)

no_chol_hd = no_hd.chol
print(np.mean(chol_hd))

tstat, pval = ttest_1samp(no_chol_hd, 240)
print(pval/2)
