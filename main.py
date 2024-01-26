
import pandas as pd
pd.set_option('display.max_columns', None)
import numpy as np
from scipy.stats import ttest_1samp, binomtest
import matplotlib.pyplot as plt

# load data
heart = pd.read_csv('heart_disease.csv')
yes_hd = heart[heart.heart_disease == 'presence']
no_hd = heart[heart.heart_disease == 'absence']
print(heart.head())

#1. Cholesterol analysis


chol_hd = yes_hd.chol
print(np.mean(chol_hd))

tstat, pval = ttest_1samp(chol_hd, 240)
print(pval/2)

no_chol_hd = no_hd.chol
print(np.mean(no_chol_hd))

tstat, pval = ttest_1samp(no_chol_hd, 240)
print(pval/2)

#2.Fasting Blood Sugar Analysis

num_patients = len(heart)
print(num_patients)

num_highfbs_patients = len(heart[heart.fbs == 1])
# found shorter option to aggregate that
num_highfbs_patient = sum(heart.fbs)
print(num_highfbs_patients)
print(num_highfbs_patient)

pval = binomtest(num_highfbs_patients, num_patients, .08, alternative='greater')
print(pval)
p_value = 0.0000467

# CONCLUSION
# If we assume significance treshold of 0.05, we have to reject null hypothesis.
# The sample was drawn from a population where more than 8% of people had fasting blood sugar higher than 120 mg/dl

#3. Trestbps prediction
#trestbps: The person’s resting blood pressure (mm Hg on admission to the hospital)
#90–120: normal 120–140: unusual 140–160: high > 160: very high

# The question is if cholesterol level is associated with resting blood pressure?

print(heart.chol.count())
print(heart.trestbps.count())

plt.scatter(x='chol', y= 'trestbps', data=heart)
plt.show()
plt.clf()

#Plot shows that there is no association between cholesterol level and resting blood pressure.