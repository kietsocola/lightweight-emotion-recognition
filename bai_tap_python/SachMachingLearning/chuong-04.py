# Load CSV Using Python Standard Library
import csv
import numpy
filename = r'd:\Workspace\nckh\DO_AN_PPNCKH\bai_tap_python\SachMachingLearning\pima-indians-diabetes.csv'
raw_data = open(filename, 'r', encoding='utf-8')
reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
x = list(reader)
data = numpy.array(x).astype('float')
print(data.shape)

# Load CSV using NumPy
from numpy import loadtxt
filename = r'd:\Workspace\nckh\DO_AN_PPNCKH\bai_tap_python\SachMachingLearning\pima-indians-diabetes.csv'
raw_data = open(filename, 'rb')
data = loadtxt(raw_data, delimiter=",")
print(data.shape)

# Load CSV from URL using NumPy
from numpy import loadtxt
from urllib.request import urlopen
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
raw_data = urlopen(url)
dataset = loadtxt(raw_data, delimiter=",", dtype=str)  # dtype=str vì file có cả chữ
print(dataset.shape)

# Load CSV using Pandas
from pandas import read_csv
filename = r'd:\Workspace\nckh\DO_AN_PPNCKH\bai_tap_python\SachMachingLearning\pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
print(data.shape)

# Load CSV using Pandas from URL
from pandas import read_csv
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['preg', 'plas', 'pres', 'skin', 'test']
data = read_csv(url, names=names)
print(data.shape)