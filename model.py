import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score

class ColorPredictor():
    '''Implements the functionality of the categorization model in a simple object'''
    def __init__(self):
        # get the processed data
        colors = preprocessing.data()
        y = colors.Name
        X = colors[['Red', 'Green', 'Blue']]

        # splitting data seems to help with accuracy, probably mitigating overfitting
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=255)
        
        # train the model
        self.model = KNeighborsClassifier(n_neighbors=7, weights='distance', algorithm='ball_tree')
        self.model.fit(X_train.values, y_train)
    def predict(self, rgb: list[int]) -> str:
        '''The object takes in a list of rgb values and returns the predicted label from its model'''
        return self.model.predict([rgb])[0]

# # this code was used to find the optimal parameters for the knn model
# if __name__ == '__main__':
#     params = {'n_neighbors': range(5, 50), 'algorithm': ['ball_tree', 'kd_tree', 'brute', 'auto']}
#     model_grid = GridSearchCV(KNeighborsClassifier(), param_grid=params, n_jobs=-1)
#     model_grid.fit(X_train, y_train)
#     print(model_grid.best_estimator_)

#     # and to test the accuracy of the model
#     model = KNeighborsClassifier(n_neighbors=7, weights='distance', algorithm='ball_tree')
#     model.fit(X_train, y_train)

#     test_preds = model.predict(X_test)
#     print(accuracy_score(y_test, test_preds))