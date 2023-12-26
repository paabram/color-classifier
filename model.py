import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score

colors = preprocessing.data()
y = colors.Name
X = colors[['Red', 'Green', 'Blue']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=255)

# this code was used to find the optimal parameters for the knn model 
# param_grid = {'n_neighbors': range(5, 50), 'algorithm': ['ball_tree', 'kd_tree', 'brute']}
# model_grid = GridSearchCV(KNeighborsClassifier(), param_grid, n_jobs=-1)
# model_grid.fit(X_train, y_train)
# print(model_grid.best_estimator_)

model = KNeighborsClassifier(n_neighbors=7, algorithm='ball_tree')
model.fit(X_train, y_train)

test_preds = model.predict(X_test)
print(accuracy_score(y_test, test_preds))