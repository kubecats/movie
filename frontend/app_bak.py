from flask import Flask, request, Response, render_template
import urllib.request as rq
import json

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/about", methods=['GET'])
def about():
    return render_template("about.html")

@app.route("/upload", methods=['GET'])
def upload():
    return render_template("upload.html")

json_str = {}
output = {}

#@app.route("/info/ns_movies/movies/{{title}}/{{movie_id}}")
@app.route("/info/<titles>", methods=['GET', 'POST'])
def info(titles):
    #json_str = rq.urlopen("https://build22.run.goorm.io/ns_movies/movies/titanic/1").read()
    #json_str = rq.urlopen("http://192.168.100.10:90/ns_movies/movies/{{title}}/{{movie_id}}").read()
    url = "http://192.168.100.10:90/ns_movies/movies/" + titles

    json_str = rq.urlopen(url).read()
    
    #json_str = rq.urlopen("http://192.168.100.10:90/ns_movies/movies/titanic").read()
    output =json.loads(json_str)

    title = output['data']['title']
    country = output['data']['country']
    genre = output['data']['genre']
    year = output['data']['year']
    rate = output['data']['rate']
    
    return render_template('info.html', h_title = title, h_country = country, h_genre = genre, h_year = year, h_rate = rate)
    #return {"genre": output['data']['genre']}
    #return output['data']['title'] + "의" + "제작 국가는" + output['data']['country'] + "이다." + " 영화 장르는"+ output['data']['genre'] + "이다"


    #return output['data']['country'], output['data']['genre']

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
