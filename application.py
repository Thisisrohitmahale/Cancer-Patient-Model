from flask import Flask, render_template, request
import joblib
app=Flask(__name__)

model = joblib.load('pick79.pkl')
print('[INFO] model loaded')

@app.route('/')
def hello_world():
    return render_template('Home.html')


@app.route('/predict' , methods = ['post'])
def predict():
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')

    output = model.predict([[int(preg),int(plas),int(pres),int(skin),int(test),int(mass),int(pedi),int(age)]])
    if output[0]==1:
        ans= 'dibatic'
    else:
        ans='not dibatic'
    return render_template('predict.html' ,prediction= f'The person is {ans}')
    # return render_template('Welcome.html' ,prediction= f'The person is {ans}')


if __name__=="__main__":
    app.run(host='0.0.0.0' ,port=8080)







## this was for practice purpose
# @app.route('/predict', methods=['post'])
# def predict():
#     first_name=request.form.get('fname')
#     last_name=request.form.get('lname')
#     email=request.form.get('email')
#     phone=request.form.get('phone')
    
#     print (first_name)
#     print(last_name)
#     print (email)
#     print (phone)
    
#     return 'Form Submitted'

# @app.route('/Welcome')
# def Welcome_page():
#     return render_template('Welcome.html')
# @app.route('/Contact')
# def Contact_page():
#     return render_template('Contact.html')
# @app.route('/Blog')
# def Blog_page():
#     return render_template('Blog.html')
# app.run(debug=True)
