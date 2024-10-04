import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

class ColorPredictor():
    '''Implements the functionality of the categorization model in a simple object'''
    def __init__(self, diagnose=False):
        # get data from preprocessor
        X, y = self.get_data()

        # splitting data helps with accuracy, and this random state splits it in such a way that the confusion matrix looks pretty good
        X_train, X_test, y_train, y_test = self.get_split(X, y)
        
        # train the model
        self.model = KNeighborsClassifier(n_neighbors=7, weights='distance', algorithm='ball_tree')
        self.model.fit(X_train.values, y_train)

        # option to show performance metrics on instantiation
        if diagnose:
            # compute and show the confusion matrix
            y_pred = self.model.predict(X_test.values)
            cm = confusion_matrix(y_test, y_pred, normalize='true')
            disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=self.model.classes_)
            disp.plot()
            plt.subplots_adjust(0.1,0,1,1)
            plt.show()

            # accuracy score
            print(accuracy_score(y_test, y_pred))

    def get_data(self):
        '''Gets the processed color data.'''
        colors = preprocessing.data()
        y = colors.Name
        X = colors[['Red', 'Green', 'Blue', 'Saturation', 'Lightness']]

        return X, y

    def get_split(self, X=None, y=None, ext=0):
        '''Returns data split into train and test sets.'''
        # allows access from outside class for grid search with ext parameter
        if ext:
            X, y = self.get_data()

        # this random state happens to make the confusion matrix look pretty good
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=255)

        return X_train, X_test, y_train, y_test

    def predict(self, rgb: list[int] = None) -> str:
        '''The object takes in a list of rgb values and returns the predicted label from its model'''
        return self.model.predict([rgb])[0]

# code for testing
if __name__ == '__main__':
    predictor = ColorPredictor(diagnose=1)

    # used a grid search to find optimal parameters
    # X_train, X_test, y_train, y_test = predictor.get_split(ext=1)
    # params = {'n_neighbors': range(5, 50), 'algorithm': ['ball_tree', 'kd_tree', 'brute', 'auto']}
    # model_grid = GridSearchCV(KNeighborsClassifier(), param_grid=params, n_jobs=-1)
    # model_grid.fit(X_train, y_train)
    # print(model_grid.best_estimator_)