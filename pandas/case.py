#место для твоего кода
import pandas as pd
df = pd.read_csv('StudentsPerformance.csv')

'''все кратко '''
#print(df.info())

'''Образование родителей'''
#print(df['parental level of education'])

'''посешение курсов'''
#ds = (df['test preparation course'] == 'none').sum()
#print(ds)
#d = (df['test preparation course'] == 'completed').sum()
#print(d)
'''прием пищи перед экзаменом'''
#ps = (df['lunch'] == 'standard').sum()
#p = (df['lunch'] == 'free/reduced').sum()
#print(ps , 'Cтандартные')
#print(p , 'Льготные')
'''баллы по экзаменам '''
#print(df['math score'].agg(['min', 'mean', 'max']))
#print(df['math score'].agg(['min', 'mean', 'max']))
#print(df['math score'].agg(['min', 'mean', 'max']))
'''гендер'''
#gs = (df['gender'] == 'male').sum()
#print(gs)
#g = (df['gender'] == 'female').sum()
#print(g)




#a = ((df['parental level of education'] != 'some college') & (df['parental level of education'] != 'high school')).sum()
#print(1000 - a)
#print(df['parental level of education'])



#d = (df['test preparation course'] == 'completed').sum()
#print(d)

#zz = df[df['test preparation course'] == 'completed']['math score'].mean()
#print(zz)
#z = df[df['test preparatio course'] == 'none']['math score'].mean()
#print(z)



#print(df['writing score'].agg(['min', 'mean', 'max']))


#l = df[df['gender'] == 'male']['math score'].mean()
#k = df[df['gender'] == 'female']['math score'].mean()
#print(l - k)


#v = ((df['race/ethnicity'] == 'group B') & (df['math score'] < 80)).sum()
#print(v)