import pickle
from flask import Flask
from flask import request

app = Flask(__name__)
        
@app.route('/')
def index():
    return "Hello, World!"
        
# http://127.0.0.1:5000/predict?text=technology    
@app.route('/predict')
def predict():
    
    text = request.args.get('text', type = str)
    
    print ('Predicting')
    print (text)
    print (type(pipe))
    print (type(text))
    
    return str(pipe.predict([text])[0])

if __name__ == '__main__':
    print ('Reading...')
    
    with open('model.out','rb') as inFile:
        pipe=pickle.load(inFile)
    print ('Read it in')        

    print ('Main')
    app.run(port=5000,debug=True)
