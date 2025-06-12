# Importar bibliotecas
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier

dados = load_breast_cancer()
X = dados.data
y = dados.target

X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.3, random_state=42)

modelo = RandomForestClassifier()
modelo.fit(X_treino, y_treino)

y_pred = modelo.predict(X_teste)
y_prob = modelo.predict_proba(X_teste)[:, 1]  # Probabilidades da classe positiva

precisao = precision_score(y_teste, y_pred)
revocacao = recall_score(y_teste, y_pred)
f1 = f1_score(y_teste, y_pred)
auc_roc = roc_auc_score(y_teste, y_prob)

print(f"Precisão: {precisao:.2f}")
print(f"Recall: {revocacao:.2f}")
print(f"F1-Score: {f1:.2f}")
print(f"AUC-ROC: {auc_roc:.2f}")
