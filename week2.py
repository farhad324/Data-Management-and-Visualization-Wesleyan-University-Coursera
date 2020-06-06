import pandas 
import numpy

data=pandas.read_csv('nesarc_pds.csv', low_memory=False)

pandas.set_option('display.float_format', lambda x: '%f'%x)

data.columns = map(str.upper, data.columns)

#Prev Question- People who suffer from "MAJOR DEPRESSION" face difficulties while working in daily life
#Refined Question- Young adults aged 18-25 suffering from "MAJOR DEPRESSION" face difficulties while working in their daily life


data1= data[(data['AGE']>=18) & (data["AGE"]<=25) & (data['S4AQ1']==1)]
sub1=data1.copy()

print("Length of the data: ",len(data))
print("Data Columns: ",len(data.columns))
print("Length of the Sub-Data: ",len(sub1))
print("Sub-Data Column: ",len(sub1.columns))

# Change the data type for chosen variables
data['S4AQ1'] = pandas.to_numeric(data['S4AQ1'])
data['AGE'] = pandas.to_numeric(data['AGE'])


#Frequency Distribution
print("AGE") 
print("Counts for AGE")
c= sub1["AGE"].value_counts(sort=False,dropna=False)
print(c)
print("Percentages for AGE")
p= sub1["AGE"].value_counts(sort=False,dropna=False, normalize=True)
print(p)
print("\n") 

print("S4AQ1")   
print("Counts for S4QA1 - 2 WEEK PERIOD OF DEPRESSION, Yes = 1")
c1= sub1["S4AQ1"].value_counts(sort=False,dropna=False)
print(c1)
print("Percentages for S4QA1 - 2 WEEK PERIOD OF DEPRESSION, Yes = 1")
p1= sub1["S4AQ1"].value_counts(sort=False,dropna=False, normalize=True)
print(p1)
print("\n") 

print("S4AQ4A14") 
print("Counts for S4AQ4A14 - TROUBLE CONCENTRATING FOR 2+ WEEKS, Yes = 1")
c2= sub1["S4AQ4A14"].value_counts(sort=False,dropna=False)
print(c2)
print("Percentages for S4AQ4A14 - TROUBLE CONCENTRATING FOR 2+ WEEKS, Yes = 1")
p2= sub1["S4AQ4A14"].value_counts(sort=False,dropna=False, normalize=True)
print(p2)
print("\n") 

print("S4AQ4A15")
print("Counts for S4AQ4A15 - DIFFICULTIES WHILE MAKING DECISIONS FOR 2+ WEEKS, Yes = 1")
c3= sub1["S4AQ4A15"].value_counts(sort=False,dropna=False)
print(c3)
print("Percentages for S4AQ4A15 - DIFFICULTIES WHILE MAKING DECISIONS FOR 2+ WEEKS, Yes = 1")
p3= sub1["S4AQ4A15"].value_counts(sort=False,dropna=False, normalize=True)
print(p3)
print("\n") 

print("S4AQ54")
print("Counts for S4AQ54 - TROUBLE WITH WORK OR TAKING CARE OF FAMILY, Yes = 1")
c4= sub1["S4AQ54"].value_counts(sort=False,dropna=False)
print(c4)
print("Percentages for S4AQ54 - TROUBLE WITH WORK OR TAKING CARE OF FAMILY, Yes = 1")
p4= sub1["S4AQ54"].value_counts(sort=False,dropna=False, normalize=True)
print(p4)
print("\n") 


##OUTPUT:

#Length of the data:  43093
#Data Columns:  3010
#Length of the Sub-Data:  1642
#Sub-Data Column:  3010
#AGE
#Counts for AGE
#18    205
#19    194
#20    195
#21    199
#22    218
#23    199
#24    235
#25    197
#Name: AGE, dtype: int64
#Percentages for AGE
#18   0.124848
#19   0.118149
#20   0.118758
#21   0.121194
#22   0.132765
#23   0.121194
#24   0.143118
#25   0.119976
#Name: AGE, dtype: float64


#S4AQ1
#Counts for S4QA1 - 2 WEEK PERIOD OF DEPRESSION, Yes = 1
#1    1642
#Name: S4AQ1, dtype: int64
#Percentages for S4QA1 - 2 WEEK PERIOD OF DEPRESSION, Yes = 1
#1   1.000000
#Name: S4AQ1, dtype: float64


#S4AQ4A14
#Counts for S4AQ4A14 - TROUBLE CONCENTRATING FOR 2+ WEEKS, Yes = 1
#2     493
#1    1144
#9       5
#Name: S4AQ4A14, dtype: int64
#Percentages for S4AQ4A14 - TROUBLE CONCENTRATING FOR 2+ WEEKS, Yes = 1
#2   0.300244
#1   0.696711
#9   0.003045
#Name: S4AQ4A14, dtype: float64


#S4AQ4A15
#Counts for S4AQ4A15 - DIFFICULTIES WHILE MAKING DECISIONS FOR 2+ WEEKS, Yes = 1
#2    776
#1    857
#9      9
#Name: S4AQ4A15, dtype: int64
#Percentages for S4AQ4A15 - DIFFICULTIES WHILE MAKING DECISIONS FOR 2+ WEEKS, Yes = 1
#2   0.472594
#1   0.521924
#9   0.005481
#Name: S4AQ4A15, dtype: float64


#S4AQ54
#Counts for S4AQ54 - TROUBLE WITH WORK OR TAKING CARE OF FAMILY, Yes = 1
#    507
#2    363
#1    768
#9      4
#Name: S4AQ54, dtype: int64
#Percentages for S4AQ54 - TROUBLE WITH WORK OR TAKING CARE OF FAMILY, Yes = 1
#    0.308770
#2   0.221072
#1   0.467722
#9   0.002436
#Name: S4AQ54, dtype: float64
