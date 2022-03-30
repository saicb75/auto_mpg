#!/usr/bin/env python
# coding: utf-8

# # Auto mpg  Model Deployment
# After analysing the given dataset, we have built and saved  model.
# 
# This Flask application is written to deploy the model in production so that users can supply automobile parameters and obtain an estimated mpg prediction.
# 
# There are two deployment models supported:
# 
# 1. Deployment to local machine
#     1. Just run this notebook in your local machine
#     
# 2. Deployment to Heroku, which needs
#     1. Procfile
#     2. requirements.txt
# 
# (search for and follow the steps to deploy the complete `deployment` folder, subfolders and contents to Heroku)

# In[ ]:


import pandas as pd
from flask import Flask, request, render_template, redirect
import pickle


# ### Load the Linear Regression  Auto mpg Model

# In[ ]:


print(f'Creating a flask app for {__name__}')
app = Flask(__name__)


# In[ ]:


def load_model(filename):
    pklfile = open(filename, 'rb')
    lr_model = pickle.load(pklfile)
    pklfile.close()
    return lr_model


# In[ ]:


lr_model_auto_mpg = load_model("models/auto_mpg_model.pkl")


# ### Create a flask app

# ### Establish Routes for Auto mpg Prediction

# In[ ]:


#Establish default route
@app.route('/')
def default():
    return redirect('/auto_mpg_input')


# In[ ]:


# Establish auto mpg routes
@app.route('/auto_mpg_input')
def auto_mpg_input():
    return render_template('auto_mpg_input.html')

@app.route('/auto_mpg_predict', methods = ['GET'])
def auto_mpg_predict():
    if request.method == 'GET':
        cylin = request.args.get('cylin')
        disp = request.args.get('disp')
        hp = request.args.get('hp')
        wt = request.args.get('wt')
        accer = request.args.get('accer')
        mod_year = request.args.get('mod_year')
        org = request.args.get('org')
        
              
        data_auto_mpg = pd.DataFrame([[cylin,disp,hp,wt,accer,mod_year,org]])
        arr_auto_mpg_predict = lr_model_auto_mpg.predict(data_auto_mpg)[0]
        arr_auto_mpg_predict = int(round(arr_auto_mpg_predict,0))
        
        return render_template('auto_mpg_predict.html',cylin = cylin, disp = disp,
                               hp = hp, wt = wt, accer = accer, 
                               mod_year = mod_year, org = org,
                               arr_auto_mpg_predict=arr_auto_mpg_predict)
    
    return "Unsupported request method,{}".format(request.method),400


# ### Run the Flask Web Server

# In[ ]:


if __name__ == '__main__':
    app.run()

