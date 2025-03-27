# View first 20 rows
from pandas import read_csv
filename = r'd:\Workspace\nckh\DO_AN_PPNCKH\bai_tap_python\SachMachingLearning\pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
peek = data.head(20)
print(peek)

# Dimensions of your data
from pandas import read_csv
filename = r'd:\Workspace\nckh\DO_AN_PPNCKH\bai_tap_python\SachMachingLearning\pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
shape = data.shape
print(shape)

# Data Types for Each Attribute
from pandas import read_csv
filename = r'd:\Workspace\nckh\DO_AN_PPNCKH\bai_tap_python\SachMachingLearning\pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
types = data.dtypes
print(types)

# Statistical Summary
from pandas import read_csv
from pandas import set_option
filename = r'd:\Workspace\nckh\DO_AN_PPNCKH\bai_tap_python\SachMachingLearning\pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
set_option('display.width', 100)
set_option('display.float_format', '{:.3f}'.format)
description = data.describe()
print(description)

# Class Distribution
from pandas import read_csv
filename = r'd:\Workspace\nckh\DO_AN_PPNCKH\bai_tap_python\SachMachingLearning\pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
class_counts = data.groupby('class').size()
print(class_counts)

# Pairwise Pearson correlations
from pandas import read_csv
from pandas import set_option
filename = r'd:\Workspace\nckh\DO_AN_PPNCKH\bai_tap_python\SachMachingLearning\pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
set_option('display.width', 100)
set_option('display.float_format', '{:.3f}'.format)
correlations = data.corr(method='pearson')
print(correlations)

# Skew for each attribute
from pandas import read_csv
filename = r'd:\Workspace\nckh\DO_AN_PPNCKH\bai_tap_python\SachMachingLearning\pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
skew = data.skew()
print(skew)