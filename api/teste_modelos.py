import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from model.avaliador import Avaliador
from model.carregador import Carregador
from model.modelo import Model

# Fixar a semente aleatória para garantir reprodutibilidade
np.random.seed(42)

# Instanciação das Classes
carregador = Carregador()
modelo = Model()
avaliador = Avaliador()

# Parâmetros    
url_dados = "database/manutencao_preventiva2.csv"
colunas = ['temp', 'proc', 'vel', 'tor', 'des']

# Carga dos dados
dataset = carregador.carregar_dados(url_dados, colunas)

# Separando em dados de entrada e saída
X = dataset.iloc[:, 0:5]
Y = dataset.iloc[:, -1]

# Normalização com MinMaxScaler
scaler_minmax = MinMaxScaler()
X_minmax = scaler_minmax.fit_transform(X)

# Padronização com StandardScaler
scaler_standard = StandardScaler()
X_standard = scaler_standard.fit_transform(X)

# Método para testar modelo SVM a partir do arquivo correspondente
def test_modelo_svm():
    # Importando modelo de SVM
    svm_path = 'ml_model/classificador.pkl'
    modelo_svm = Model.carrega_modelo(svm_path)

    # Obtendo as métricas do SVM para dados com normalização MinMaxScaler
    acuracia_svm_minmax = avaliador.avaliar(modelo_svm, X_minmax, Y)
    
    # Obtendo as métricas do SVM para dados com padronização StandardScaler
    acuracia_svm_standard = avaliador.avaliar(modelo_svm, X_standard, Y)
    
    # Testando as métricas do SVM com normalização MinMaxScaler
    assert acuracia_svm_minmax >= 0.7
    
    # Testando as métricas do SVM com padronização StandardScaler
    assert acuracia_svm_standard >= 0.7
   