# Auto MPG Data Set
_Note: (This data set is available in UCI at https://archive.ics.uci.edu/ml/datasets/auto+mpg An excerpt of the problem statement is reproduced here for convenience.)_

**Abstract:** Revised from CMU StatLib library, data concerns city-cycle fuel consumption

#### Data Set Information:

This dataset is a slightly modified version of the dataset provided in the StatLib library. In line with the use by Ross Quinlan (1993) in predicting the attribute "mpg", 8 of the original instances were removed because they had unknown values for the "mpg" attribute. The original dataset is available in the file "auto-mpg.data-original".

"The data concerns city-cycle fuel consumption in miles per gallon, to be predicted in terms of 3 multivalued discrete and 5 continuous attributes." (Quinlan, 1993)


#### Attribute Information:

1. mpg: continuous (target variable)
2. cylinders: multi-valued discrete
3. displacement: continuous
4. horsepower: continuous
5. weight: continuous
6. acceleration: continuous
7. model year: multi-valued discrete
8. origin: multi-valued discrete
9. car name: string (unique for each instance)


## Approach for Auto mpg model


Our project adopts a folder structure as follows:

<pre>
auto-mpg
    |________ ml_models
        |________ datasets
        |________ models
        |________ .ipynb file
        
    |________ heroku
        |________ models
        |________ templates
        
</pre>

### Develop an ML Model

Developing an ML model involves a number of steps. Let us adopt the following Machine Learning Pipeline:

1. Sanity Check 
2. EDA/Preprocessing
3. Feature Engineering
4. Model Building
5. Model Saving
6. Model Deployment

Once the model is deployed, the pipeline extends to include the below steps:

7. Model in Production
8. Observe model behaviour
9. Obtain updated datasets
10. Redo steps 1..9 if required

Note: these extended steps are not covered in this exercise

### Results obtained

1. Linear Regression Accuracy = 88.21
2. Logistic Regression Accuracy = 55.69%, 61.35% (cross-validation), 65.82% (K-fold, k=5)
3. Decision Tree Accuracy = 58.22%
4. Random Forest Accuracy = 68.35%

Accordingly, the linear regression model was saved as a pickle file and used for deployment.

### Deployment

The saved model will be deployed and made accessible to users for mpg prediction. A Flask application is developed for this purpose. Two approaches are covered:

1. Deployment on local machine
2. Deployment on Heroku - requirements.txt and Procfile are provided.

### Way Forward

The linear model developed here show an accuracy of about 88%. Further improvement can be attempted using other ML techniques like Deep Learning.