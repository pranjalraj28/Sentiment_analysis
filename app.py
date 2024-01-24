

from flask import Flask




from flask import Flask, render_template, request
from model.sentiment_model import predict_sentiment

app = Flask(__name__, template_folder='app/templates')

from app import routes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    tweet = request.form['tweet']
    result = predict_sentiment(tweet)
    return render_template('index.html', tweet=tweet, result=result)

if __name__ == '__main__':
    app.run(debug=True)
