import joblib
#loading the model

dib_model = joblib.load('pick79.pkl')

output = dib_model.predict([[1 , 85, 66, 1,1,1,1,1]])


if output[0]== 0:
    print ('Not a diabetic patient')
   
else:
    print ('The diabetic Patient')
