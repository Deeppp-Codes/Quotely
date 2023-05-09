from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/home")
def home():
    category = 'money'
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': '9odNchnb5W73GSOneOvAaw==uSj9pAT0131VJkXJ'})

    if response.status_code == requests.codes.ok:
        response_dict = response.json()
        quote = response_dict[0]["quote"]
        print(quote)

    else:
        print("Error:", response.status_code, response.text)

    return render_template("index.html", quote=quote)

@app.route('/about')
def about():
    return render_template("dev.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')


