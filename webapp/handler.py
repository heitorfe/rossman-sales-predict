import pickle
import pandas as pd
from flask import Flask, request, Response
from rossmann.Rossmann import Rossmann
import os

#loading model
model = pickle.load(open('model/model_rossmann.pkl', 'rb'))

#initialize API
app = Flask(__name__)
@app.route( '/rossmann/predict', methods=['POST'] )
def rossmann_predict():
    test_json = request.get_json()
    if test_json: # there is data
        if isinstance( test_json, dict ): # unique example
            test_raw = pd.DataFrame( test_json, index=[0] )
            
        else: # multiple example
            test_raw = pd.DataFrame( test_json, columns = test_json[0].keys() )
            
        # Instantiate rossmann class
        pipeline = Rossmann()
        
        # data cleaning
        df = pipeline.data_cleaning( test_raw )
        
        # feature engineering
        df = pipeline.feature_engineering( df )
        
        # data transformation
        df = pipeline.data_transformation( df )
        
        # get prediction
        df_response = pipeline.get_prediction( model, test_raw, df )
        
        return df_response
    
    else:
        return Response( '{}', status=200, mimetype='application/json' )

if __name__ == '__main__':
    port = os.environ.get( 'PORT', 5000)
    app.run( host='0.0.0.0', port=port )
