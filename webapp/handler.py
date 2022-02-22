import pickle
import pandas as pd
from flask import Flask, request, Response
from rossmann.Rossmann import Rossmann
import os
print('teste1')
#loading model
model = pickle.load(open('model/model_rossmann.pkl', 'rb'))
print('teste2')

#initialize API
app = Flask(__name__)
print('teste3')
@app.route( '/rossmann/predict', methods=['POST'] )
def rossmann_predict():
    print('sdkjs')
    test_json = request.get_json()
    print('dfdsf')
    
    if test_json: # there is data
        if isinstance( test_json, dict ): # unique example
            test_raw = pd.DataFrame( test_json, index=[0] )
            
        else: # multiple example
            test_raw = pd.DataFrame( test_json, columns = test_json[0].keys() )
            
        # Instantiate rossmann class
        pipeline = Rossmann()
        
        # data cleaning
        df1 = pipeline.data_cleaning( test_raw )
        
        # feature engineering
        df2 = pipeline.feature_engineering( df1 )
        
        # data transformation
        df3 = pipeline.data_transformation( df2 )
        
        # get prediction
        df_response = pipeline.get_prediction( model, test_raw, df3 )
        
        return df_response
    
    else:
        return Response( '{}', status=200, mimetype='application/json' )

if __name__ == '__main__':
    port = os.environ.get( 'PORT', 5000)
    app.run( host='0.0.0.0', port=port )
