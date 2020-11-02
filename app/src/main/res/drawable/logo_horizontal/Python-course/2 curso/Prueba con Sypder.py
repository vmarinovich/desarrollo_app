
# Importar el data set
dataset = pd.read_csv('zData.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 3].values



