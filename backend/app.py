from flask import Flask, request, Response, render_template
from flask_restx import Resource, Api, fields, Namespace
from flask import abort, jsonify


app = Flask(__name__)
#api = Api(app)
api = Api(app, version='1.0', title='영화 정보 API 문서', description='Swagger 문서', doc="/api-docs")

ns_movies = api.namespace('ns_movies', description='Movie APIs')

movie_data = api.model(
    'Movie Data',
    { 
      "title": fields.String(description="movie title", required=True),
      "country": fields.String(description="movie country", required=True),
      "genre": fields.String(description="movie genre", required=True),
      "year": fields.Integer(description="movie released year", required=True),
      "rate": fields.Float(description="movie rate", required=True)
    }
)

movie_info = {}
number_of_movies = 0

@ns_movies.route('/movies')
class movies(Resource):
  def get(self):
    return {
        'number_of_movies': number_of_movies,
        'movie_info': movie_info
    }

@ns_movies.route('/movies/<string:title>')
class movie_title_model(Resource):
  def get(self, title):
    if not title in movie_info.keys():
      abort(404, description=f"title {title} doesn't exists")

    return {
        'data': movie_info[title]
    }

  @api.expect(movie_data) # body
  def post(self, title):

    params = request.get_json() # get body json
    movie_info[title] = params
    global number_of_movies
    number_of_movies += 1
  
    return Response(status=200)
  
  
  def delete(self, title):
    if not title in movie_info.keys():
      abort(404, description=f"title {title} doesn't exists")

    del movie_info[title]
    global number_of_movies
    number_of_movies -= 1

    return Response(status=200)


  @api.expect(movie_data)
  def put(self, title):
    global movie_info

    if not title in movie_info.keys():
      abort(404, description=f"title {title} doesn't exists")
    
    params = request.get_json()
    movie_info[title] = params
    
    return Response(status=200)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
