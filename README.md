# Heart Diesease Reserch 
## Introduction 

In this project I use python 3.11 and following moduled:
+ pandas
+ scipy.stats
+ matplotlib.pyplot
+ statsmodels.api

Project covers five topics:
+ cholesterol analsis
+ fasting blood sugar analysis
+ resting blood pressure predictions
+ maximum heart rate prediction

## Analyse 
1. For this analyse I divded dataset into 2 parts:
+ one representing people with heart disease
+ one representing people without heart disease

Knowing the mean cholesterol level for US population equeal to 240 mg/dl we can  check cholesterol levels in our sample.

The mean cholesterol level for people without heart disease is equal to 242 mg/dl

The mean cholesterol level for people without heart disease is equal to 251 mg/dl

The question is - is this cholesterol level relatively higher than  the population one?

In one sample T-test can help us to fint the right answer.

tstat, pval = ttest_1samp(chol_heartdisease, 240)

pval = 0.0071 = 0.7%

Assuming that the significance threshold for our analysis is equal to 5%, we see that the ***average cholesterol level*** in the group of heart patients ***is significantly higher*** than in the general population.

tstat, pval = ttest_1samp(no_chol_heartdisease, 240)

pval = 0.53 = 0.53%

Once again assuming that significance treshold for analysis id equal to 5%, we see that average cholesterol level in the sample without heart diseases is the same as in the general population.

2. In this part we analyse fbs parameter - fbs: The person’s fasting blood sugar (> 120 mg/dl, 1 = true; 0 = false)
The question is if sample fbs is significance higher than 8% ? Null hypothesis is that sample fbs over 120 mg/dl is equal 8%. Alternative hypothesis is that sample fsb over 120 mg/dl is higher than 8%.
Having dataset with two values ( 0,1 ) i decided to use binom test. I know that in population US 8% of people suffer fbs.

pval = binomtest(num_highfbs_patients, num_patients, .08, alternative='greater') = 0.0000467

If we assume significance treshold of 0.05, we have to reject null hypothesis. The sample was drawn from a population where more than 8% of people had fasting blood sugar higher than 120 mg/dl

3. Trestbps prediction
trestbps: The person’s resting blood pressure (mm Hg on admission to the hospital)
#90–120: normal 120–140: unusual 140–160: high > 160: very high

The question is if cholesterol level is associated with resting blood pressure?

![cholesterol](https://github.com/GrzegorzCiepiel/Heart-Disease-Research/assets/135313652/70fbe51c-a317-45b0-93a8-f7ddc47a20c2)

#Plot shows that there is no association between cholesterol level and resting blood pressure.

4.  Simple linear regression on sample:
The question is if thalach (The person’s maximum heart rate achieved) is associated with age?

To answer this question firstly I plot ages vs max heart rates:
![age heart rate](https://github.com/GrzegorzCiepiel/Heart-Disease-Research/assets/135313652/b3b0d5ef-89bb-43f1-ae0a-1102144589d0)

As we can see there is correlation between these two so I try to analyse further:

I use OLS.from_formula method from statsmodels.api  to get fitted values. Then using fitted values I plot a line showing correlation between thelach and age.

![linear regresion](https://github.com/GrzegorzCiepiel/Heart-Disease-Research/assets/135313652/c17e850c-441f-4f6f-92e5-c151d35673a6)







## Conclusions
1. The ***average cholesterol level*** in the group of heart patients ***is significantly higher*** than in the general population. There is correlation between high cholesterol level and heart diseases.
2. The sample was drawn from a population where more than 8% of people had fasting blood sugar higher than 120 mg/dl
3. According to a sample there is ***no association between cholesterol level and resting blood pressure***.
4. The person’s ***maximum heart rate*** achieved ***is associated with*** persons's ***age***.
