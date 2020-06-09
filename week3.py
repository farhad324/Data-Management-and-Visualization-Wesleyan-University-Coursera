
#Question: Percentage of facing difficulties caused by different reasons of MAJOR DEPRESSION

#By using the variables 

#c:- AGE → AGE
# S4AQ1 → EVER HAD 2-WEEK PERIOD WHEN FELT SAD, BLUE, DEPRESSED, OR DOWN MOST OF TIME, 
#c2:- S4AQ4A14→HAD TROUBLE CONCENTRATING/KEEPING MIND ON THINGS MOST DAYS FOR 2+ WEEKS , 
#c3:- S4AQ4A15→ FOUND IT HARDER TO MAKE DECISIONS MOST OF THE TIME FOR 2+ WEEKS, 
#c4:-S4AQ54→ HAD TROUBLE DOING THINGS SUPPOSED TO DO--LIKE WORKING, DOING SCHOOLWORK, OR TAKING CARE OF HOME/FAMILY
#S4AQ10CR→ ONLY/ANY EPISODE OF <2 MONTHS IN LAST 12 MONTHS HAPPENED AFTER SOMEONE CLOSE DIED 
#S4AQ15CR→ ONLY/ANY EPISODE IN LAST 12 MONTHS BEGAN AFTER DRINKING/DRUG USE
#S4AQ22CR→ ONLY/ANY EPISODE IN LAST 12 MONTHS RELATED TO ILLNESS 
#From the “NESARC” dataset I’m interested in seeing if people who suffer from “MAJOR DEPRESSION” face difficulties while working in daily life.
#Current Hypothesis is that Young adults aged 18-25, who are suffering from "MAJOR DEPRESSION" because of different reasons face difficulties while working in their daily life.

import pandas 
import numpy

data=pandas.read_csv('nesarc_pds.csv', low_memory=False)

pandas.set_option('display.float_format', lambda x: '%f'%x)

data.columns = map(str.upper, data.columns)

data['S4AQ1'] = pandas.to_numeric(data['S4AQ1'],errors='coerce')
data['AGE'] = pandas.to_numeric(data['AGE'],errors='coerce')
data['S4AQ4A14'] = pandas.to_numeric(data['S4AQ4A14'],errors='coerce')
data['S4AQ4A15'] = pandas.to_numeric(data['S4AQ4A15'],errors='coerce')
data['S4AQ54'] = pandas.to_numeric(data['S4AQ54'],errors='coerce')
data['S4AQ10CR'] = pandas.to_numeric(data['S4AQ10CR'],errors='coerce')
data['S4AQ15CR'] = pandas.to_numeric(data['S4AQ15CR'],errors='coerce')
data['S4AQ22CR'] = pandas.to_numeric(data['S4AQ22CR'],errors='coerce')

data1= data[((data['AGE']>=18)&(data["AGE"]<=25)&(data['S4AQ1']==1))]
sub1=data1.copy()
sub1= sub1.replace(to_replace = 9, value =numpy.nan)
sub1['NA']=sub1['S4AQ10CR']+sub1['S4AQ15CR']+sub1['S4AQ22CR']
def REASON (row):
    if(row["S4AQ10CR"]==1):
        return 1
    elif(row["S4AQ15CR"]==1):
        return 2
    elif(row["S4AQ22CR"]==1):
        return 3
    elif(row["NA"]==6):
        return 4
    elif(row["NA"]!=6):
        return 5


sub1["REASON"] = sub1.apply(lambda row: REASON(row),axis=1)    
sub2=sub1[['NA','S4AQ10CR','S4AQ15CR','S4AQ22CR','S4AQ4A14','S4AQ4A15','S4AQ54','REASON']]
#a=sub2.head(n=180)
#print(a)
print("Frequency Table of REASON(s)")
print('Someone\'s Death = 1, Drug Abuse = 2, Illness = 3, NaN = 4, Multiple = 5')
c=sub2["REASON"].value_counts(sort=False,dropna=False)
print(c)

print("S4AQ4A14") 
print("Counts for S4AQ4A14 - TROUBLE CONCENTRATING FOR 2+ WEEKS, Yes = 1")
c2= sub2["S4AQ4A14"].value_counts(sort=False,dropna=False)
print(c2)
print("Percentages for S4AQ4A14 - TROUBLE CONCENTRATING FOR 2+ WEEKS, Yes = 1")
p2= sub2["S4AQ4A14"].value_counts(sort=False,dropna=False, normalize=True)*100
print(p2)
print("\n") 

print("S4AQ4A15")
print("Counts for S4AQ4A15 - DIFFICULTIES WHILE MAKING DECISIONS FOR 2+ WEEKS, Yes = 1")
c3= sub2["S4AQ4A15"].value_counts(sort=False,dropna=False)
print(c3)
print("Percentages for S4AQ4A15 - DIFFICULTIES WHILE MAKING DECISIONS FOR 2+ WEEKS, Yes = 1")
p3= sub2["S4AQ4A15"].value_counts(sort=False,dropna=False, normalize=True)*100
print(p3)
print("\n") 

print("S4AQ54")
print("Counts for S4AQ54 - TROUBLE WITH WORK OR TAKING CARE OF FAMILY, Yes = 1")
c4= sub2["S4AQ54"].value_counts(sort=False,dropna=False)
print(c4)
print("Percentages for S4AQ54 - TROUBLE WITH WORK OR TAKING CARE OF FAMILY, Yes = 1")
p4= sub2["S4AQ54"].value_counts(sort=False,dropna=False, normalize=True)*100 
print(p4)
print("\n") 

print("Facing difficulties during work because of different reasons")
print('TROUBLE CONCENTRATING FOR 2+ WEEKS, Someone\'s Death = 1, Drug Abuse = 2, Illness = 3, NaN = 4, Multiple = 5' )
print(pandas.crosstab(sub2['REASON'],sub2['S4AQ4A14']))
print("\n") 
print('DIFFICULTIES WHILE MAKING DECISIONS FOR 2+ WEEKS, Someone\'s Death = 1, Drug Abuse = 2, Illness = 3, NaN = 4, Multiple = 5')
print(pandas.crosstab(sub2['REASON'],sub2['S4AQ4A15']))
print("\n") 
print('TROUBLE WITH WORK OR TAKING CARE OF FAMILY, Someone\'s Death = 1, Drug Abuse = 2, Illness = 3, NaN = 4, Multiple = 5')
print(pandas.crosstab(sub2['REASON'],sub2['S4AQ54']))
print("\n") 

print('Percentage of TROUBLE CONCENTRATING FOR 2+ WEEKS, Someone\'s Death = 1, Drug Abuse = 2, Illness = 3, NaN = 4, Multiple = 5' )
print(pandas.crosstab(sub2['REASON'],sub2['S4AQ4A14'],normalize='index')*100)
print("\n") 
print('Percentage of DIFFICULTIES WHILE MAKING DECISIONS FOR 2+ WEEKS, Someone\'s Death = 1, Drug Abuse = 2, Illness = 3, NaN = 4, Multiple = 5')
print(pandas.crosstab(sub2['REASON'],sub2['S4AQ4A15'],normalize='index')*100)
print("\n")
print('Percentage of TROUBLE WITH WORK OR TAKING CARE OF FAMILY, Someone\'s Death = 1, Drug Abuse = 2, Illness = 3, NaN = 4, Multiple = 5') 
print(pandas.crosstab(sub2['REASON'],sub2['S4AQ54'],normalize='index')*100)
print("\n") 

#OUTPUT:
#Frequency Table of REASON(s)
#Someone's Death = 1, Drug Abuse = 2, Illness = 3, NaN = 4, Multiple = 5
#1      97
#2      50
#3      70
#4     240
#5    1185
#Name: REASON, dtype: int64
#S4AQ4A14
#Counts for S4AQ4A14 - TROUBLE CONCENTRATING FOR 2+ WEEKS, Yes = 1
#2.000000     493
#1.000000    1144
#nan            5
#Name: S4AQ4A14, dtype: int64
#Percentages for S4AQ4A14 - TROUBLE CONCENTRATING FOR 2+ WEEKS, Yes = 1
#2.000000   30.024361
#1.000000   69.671133
#nan         0.304507
#Name: S4AQ4A14, dtype: float64


#S4AQ4A15
#Counts for S4AQ4A15 - DIFFICULTIES WHILE MAKING DECISIONS FOR 2+ WEEKS, Yes = 1
#2.000000    776
#1.000000    857
#nan           9
#Name: S4AQ4A15, dtype: int64
#Percentages for S4AQ4A15 - DIFFICULTIES WHILE MAKING DECISIONS FOR 2+ WEEKS, Yes = 1
#2.000000   47.259440
#1.000000   52.192448
#nan         0.548112
#Name: S4AQ4A15, dtype: float64


#S4AQ54
#Counts for S4AQ54 - TROUBLE WITH WORK OR TAKING CARE OF FAMILY, Yes = 1
#2.000000    363
#nan         511
#1.000000    768
#Name: S4AQ54, dtype: int64
#Percentages for S4AQ54 - TROUBLE WITH WORK OR TAKING CARE OF FAMILY, Yes = 1
#2.000000   22.107186
#nan        31.120585
#1.000000   46.772229
#Name: S4AQ54, dtype: float64


#Facing difficulties during work because of different reasons
#TROUBLE CONCENTRATING FOR 2+ WEEKS, Someone's Death = 1, Drug Abuse = 2, Illness = 3, NaN = 4, Multiple = 5
#S4AQ4A14  1.000000  2.000000
#REASON                      
#1               85        12
#2               47         3
#3               61         9
#4              212        28
#5              739       441


#DIFFICULTIES WHILE MAKING DECISIONS FOR 2+ WEEKS, Someone's Death = 1, Drug Abuse = 2, Illness = 3, NaN = 4, Multiple = 5
#S4AQ4A15  1.000000  2.000000
#REASON                      
#1               65        32
#2               44         6
#3               44        26
#4              154        86
#5              550       626


#TROUBLE WITH WORK OR TAKING CARE OF FAMILY, Someone's Death = 1, Drug Abuse = 2, Illness = 3, NaN = 4, Multiple = 5
#3S4AQ54  1.000000  2.000000
#REASON                    
#1             64        33
#2             36        14
#3             49        21
#4            156        84
#5            463       211


#Percentage of TROUBLE CONCENTRATING FOR 2+ WEEKS, Someone's Death = 1, Drug Abuse = 2, Illness = 3, NaN = 4, Multiple = 5
#S4AQ4A14  1.000000  2.000000
#REASON                      
#1        87.628866 12.371134
#2        94.000000  6.000000
#3        87.142857 12.857143
#4        88.333333 11.666667
#5        62.627119 37.372881


#Percentage of DIFFICULTIES WHILE MAKING DECISIONS FOR 2+ WEEKS, Someone's Death = 1, Drug Abuse = 2, Illness = 3, NaN = 4, Multiple = 5
#S4AQ4A15  1.000000  2.000000
#REASON                      
#1        67.010309 32.989691
#2        88.000000 12.000000
#3        62.857143 37.142857
#4        64.166667 35.833333
#5        46.768707 53.231293


#Percentage of TROUBLE WITH WORK OR TAKING CARE OF FAMILY, Someone's Death = 1, Drug Abuse = 2, Illness = 3, NaN = 4, Multiple = 5
#S4AQ54  1.000000  2.000000
#REASON                    
#1      65.979381 34.020619
#2      72.000000 28.000000
#3      70.000000 30.000000
#4      65.000000 35.000000
#5      68.694362 31.305638

#We can conclude that:-
# For REASON = Someone's Death-
# Almost 88% of the sufferer had trouble concentrating
# Almost 67% of the sufferer had trouble making decisions
# Almost 66% of the sufferer had trouble with their work and taking care of their families

# For REASON = Drug Abuse-
# Almost 94% of the sufferer had trouble concentrating
# Almost 88% of the sufferer had trouble making decisions
# Almost 72% of the sufferer had trouble with their work and taking care of their families

# For REASON = Illness-
# Almost 87% of the sufferer had trouble concentrating
# Almost 63% of the sufferer had trouble making decisions
# Almost 70% of the sufferer had trouble with their work and taking care of their families
