#Question: Percentage of facing difficulties caused by different reasons of MAJOR DEPRESSION
#By using the variables
#c:- REASON → REASON S4AQ1 → EVER HAD 2-WEEK PERIOD WHEN FELT SAD, BLUE, DEPRESSED, OR DOWN MOST OF TIME, 
#c2:- S4AQ4A14→HAD TROUBLE CONCENTRATING/KEEPING MIND ON THINGS MOST DAYS FOR 2+ WEEKS , 
#c3:- S4AQ4A15→ FOUND IT HARDER TO MAKE DECISIONS MOST OF THE TIME FOR 2+ WEEKS, 
#c4:-S4AQ54→ HAD TROUBLE DOING THINGS SUPPOSED TO DO–LIKE WORKING, DOING SCHOOLWORK, OR TAKING CARE OF HOME/FAMILY
#S4AQ10CR→ ONLY/ANY EPISODE OF <2 MONTHS IN LAST 12 MONTHS HAPPENED AFTER SOMEONE CLOSE DIED 
#S4AQ15CR→ ONLY/ANY EPISODE IN LAST 12 MONTHS BEGAN AFTER DRINKING/DRUG USE 
#S4AQ22CR→ ONLY/ANY EPISODE IN LAST 12 MONTHS RELATED TO ILLNESS From the “NESARC” dataset I’m interested in seeing if people who suffer from “MAJOR DEPRESSION” face difficulties while working in daily life. 
#Current Hypothesis is that Young adults aged 18-25, who are suffering from “MAJOR DEPRESSION” because of different reasons face difficulties while working in their daily life.
#function = REASON helps us to collect all the reasons in one dataframe
#We can conclude that:-

#1. From Graph- Trouble Concentrating=
#a. Drug abuse has the strongest impact on losing concentration
#b. The graph is a uniform graph

#2. From Graph- Trouble Making Decisions=
#a. Drug abuse has the strongest impact on losing concentration
#b. The graph is a unimodal graph

#3. From Graph- Trouble taking care pf family and work=
#a. Drug abuse has the strongest impact on losing concentration
#b. The graph is a uniform graph



import pandas 
import numpy
import seaborn
import matplotlib.pyplot as plt

datax=pandas.read_csv('nesarc_pds.csv', low_memory=False)

pandas.set_option('display.float_format', lambda x: '%f'%x)
pandas.set_option('display.max_columns', None)
pandas.set_option('display.max_rows', None)

datax.columns = map(str.upper, datax.columns)

datax['S4AQ1'] = pandas.to_numeric(datax['S4AQ1'],errors='coerce')
datax['AGE'] = pandas.to_numeric(datax['AGE'],errors='coerce')
datax['S4AQ4A14'] = pandas.to_numeric(datax['S4AQ4A14'],errors='coerce')
datax['S4AQ4A15'] = pandas.to_numeric(datax['S4AQ4A15'],errors='coerce')
datax['S4AQ54'] = pandas.to_numeric(datax['S4AQ54'],errors='coerce')
datax['S4AQ10CR'] = pandas.to_numeric(datax['S4AQ10CR'],errors='coerce')
datax['S4AQ15CR'] = pandas.to_numeric(datax['S4AQ15CR'],errors='coerce')
datax['S4AQ22CR'] = pandas.to_numeric(datax['S4AQ22CR'],errors='coerce')


data1= datax[((datax['AGE']>=18)&(datax["AGE"]<=25)&(datax['S4AQ1']==1))]
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
    else:
        return 4
   

sub1["REASON"] = sub1.apply(lambda row: REASON(row),axis=1)    
sub2=sub1[['NA','S4AQ10CR','S4AQ15CR','S4AQ22CR','S4AQ4A14','S4AQ4A15','S4AQ54','REASON']]
#a=sub2.head(n=180)
#print(a)
print("Frequency Table of REASON(s)")
print('Someone\'s Death = 1, Drug Abuse = 2, Illness = 3, NaN = 4')
c=sub2["REASON"].value_counts(sort=False,dropna=False)
print(c)


sub2['S4AQ4A14'] = sub2['S4AQ4A14'].astype('category')

print("S4AQ4A14") 
print("Counts for S4AQ4A14 - TROUBLE CONCENTRATING FOR 2+ WEEKS, Yes = 1")
c2= sub2["S4AQ4A14"].value_counts(sort=False,dropna=False)
print(c2)
print("Percentages for S4AQ4A14 - TROUBLE CONCENTRATING FOR 2+ WEEKS, Yes = 1")
p2= sub2["S4AQ4A14"].value_counts(sort=False,dropna=False, normalize=True)*100
print(p2)
print("\n")

print('Describing the S4AQ4A14 variable')
desc2=sub2["S4AQ4A14"].describe()
print(desc2)


sub2['S4AQ4A14'] = pandas.to_numeric(sub2['S4AQ4A14'],errors='coerce')
sub2["REASON"]= sub2["REASON"].replace(to_replace = 4, value =numpy.nan)
sub2["REASON"].dropna()

def CONCENTRATE (row):
    if(row["S4AQ4A14"]==1):
        return 1
    elif(row["S4AQ4A14"]!=1):
        return 0
    
sub2['CONCENTRATE']=sub2.apply(lambda row: CONCENTRATE (row),axis=1)

seaborn.factorplot(x="REASON",y="CONCENTRATE",data=sub2,kind='bar',ci=None )
plt.xlabel('Reasons; Someone\'s Death = 1, Drug Abuse = 2, Illness = 3')
plt.ylabel('TROUBLE CONCENTRATING FOR 2+ WEEKS')
plt.title('TROUBLE CONCENTRATING FOR 2+ WEEKS from NESARC')

sub2['S4AQ4A15'] = sub2['S4AQ4A15'].astype('category')
print("S4AQ4A15")
print("Counts for S4AQ4A15 - DIFFICULTIES WHILE MAKING DECISIONS FOR 2+ WEEKS, Yes = 1")
c3= sub2["S4AQ4A15"].value_counts(sort=False,dropna=False)
print(c3)
print("Percentages for S4AQ4A15 - DIFFICULTIES WHILE MAKING DECISIONS FOR 2+ WEEKS, Yes = 1")
p3= sub2["S4AQ4A15"].value_counts(sort=False,dropna=False, normalize=True)*100
print(p3)
print("\n") 

print('Describing the S4AQ4A15 variable')
desc22=sub2["S4AQ4A15"].describe()
print(desc22)


sub2['S4AQ4A15'] = pandas.to_numeric(sub2['S4AQ4A15'],errors='coerce')

def DECISIONS (row):
    if(row["S4AQ4A15"]==1):
        return 1
    elif(row["S4AQ4A15"]!=1):
        return 0
    
sub2['DECISIONS']=sub2.apply(lambda row: DECISIONS (row),axis=1)
seaborn.factorplot(x="REASON",y="DECISIONS",data=sub2,kind='bar',ci=None )
plt.xlabel('Reasons; Someone\'s Death = 1, Drug Abuse = 2, Illness = 3')
plt.ylabel('DIFFICULTIES WHILE MAKING DECISIONS FOR 2+ WEEKS')
plt.title('DIFFICULTIES WHILE MAKING DECISIONS FOR 2+ WEEKS from NESARC')

print("S4AQ54")
print("Counts for S4AQ54 - TROUBLE WITH WORK OR TAKING CARE OF FAMILY, Yes = 1")
c4= sub2["S4AQ54"].value_counts(sort=False,dropna=False)
print(c4)
print("Percentages for S4AQ54 - TROUBLE WITH WORK OR TAKING CARE OF FAMILY, Yes = 1")
p4= sub2["S4AQ54"].value_counts(sort=False,dropna=False, normalize=True)*100 
print(p4)
print("\n") 

sub2['S4AQ54'] = pandas.to_numeric(sub2['S4AQ54'],errors='coerce')

def FAMWORK (row):
    if(row["S4AQ54"]==1):
        return 1
    elif(row["S4AQ54"]!=1):
        return 0
    
sub2['FAMWORK']=sub2.apply(lambda row: FAMWORK (row),axis=1)
seaborn.factorplot(x="REASON",y="FAMWORK",data=sub2,kind='bar',ci=None )
plt.xlabel('Reasons; Someone\'s Death = 1, Drug Abuse = 2, Illness = 3')
plt.ylabel('TROUBLE WITH WORK OR TAKING CARE OF FAMILY')
plt.title('TROUBLE WITH WORK OR TAKING CARE OF FAMILY from NESARC')

print("Facing difficulties during work because of different reasons")
print('TROUBLE CONCENTRATING FOR 2+ WEEKS, Someone\'s Death = 1, Drug Abuse = 2, Illness = 3, NaN = 4' )
print(pandas.crosstab(sub2['REASON'],sub2['S4AQ4A14']))
print("\n") 
print('DIFFICULTIES WHILE MAKING DECISIONS FOR 2+ WEEKS, Someone\'s Death = 1, Drug Abuse = 2, Illness = 3, NaN = 4')
print(pandas.crosstab(sub2['REASON'],sub2['S4AQ4A15']))
print("\n") 
print('TROUBLE WITH WORK OR TAKING CARE OF FAMILY, Someone\'s Death = 1, Drug Abuse = 2, Illness = 3, NaN = 4')
print(pandas.crosstab(sub2['REASON'],sub2['S4AQ54']))
print("\n") 

print('Percentage of TROUBLE CONCENTRATING FOR 2+ WEEKS, Someone\'s Death = 1, Drug Abuse = 2, Illness = 3, NaN = 4' )
print(pandas.crosstab(sub2['REASON'],sub2['S4AQ4A14'],normalize='index')*100)
print("\n") 
print('Percentage of DIFFICULTIES WHILE MAKING DECISIONS FOR 2+ WEEKS, Someone\'s Death = 1, Drug Abuse = 2, Illness = 3, NaN = 4')
print(pandas.crosstab(sub2['REASON'],sub2['S4AQ4A15'],normalize='index')*100)
print("\n")
print('Percentage of TROUBLE WITH WORK OR TAKING CARE OF FAMILY, Someone\'s Death = 1, Drug Abuse = 2, Illness = 3, NaN = 4') 
print(pandas.crosstab(sub2['REASON'],sub2['S4AQ54'],normalize='index')*100)
print("\n")


