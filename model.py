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
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.33, random_state=463)
        
        # train the model
        self.model = KNeighborsClassifier(n_neighbors=7, weights='distance', algorithm='ball_tree')
        self.model.fit(self.X_train.values, self.y_train)
    def predict(self, rgb: list[int] = None) -> str:
        '''The object takes in a list of rgb values and returns the predicted label from its model'''
        # default to testing values if no rgb is passed in
        if rgb == None:
            rgb = self.X_test.values
            return self.model.predict(rgb)
        
        return self.model.predict([rgb])[0]

# code for testing
if __name__ == '__main__':
    predictor = ColorPredictor()

    # used a grid search to find optimal parameters
    # params = {'n_neighbors': range(5, 50), 'algorithm': ['ball_tree', 'kd_tree', 'brute', 'auto']}
    # model_grid = GridSearchCV(KNeighborsClassifier(), param_grid=params, n_jobs=-1)
    # model_grid.fit(predictor.X_train, predictor.y_train)
    # print(model_grid.best_estimator_)

    # checking accuracy of predictions
    # tested value accuracy was 83.75%
    test_preds = predictor.predict()
    print(accuracy_score(predictor.y_test, test_preds))