from flask import Flask, request, Response, render_template
from flask_restx import Resource, Api, fields, Namespace
from flask import abort, jsonify


app = Flask(__name__)
api = Api(app)

ns_movies = api.namespace('ns_movies', description='Movie APIs')

movie_data = api.model(
    'Movie Data',
    {
      "title": fields.String(description="movie title", required=True),
      "year": fields.Integer(description="movie released year", required=True),
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
class movies_title(Resource):

  # 영화 정보 조회
  def get(self, title):
    if not title in movie_info.keys():
      abort(404, description=f"title {title} doesn't exist")
    data = movie_info[title]

    return {
        'number_of_movies': len(data.keys()),
        'data': data
    }


  # 영화 정보 추가
  def post(self, title):
    if title in movie_info.keys():
      abort(409, description=f"title {title} already exists")

    movie_info[title] = dict()
    return Response(status=201)


  # 영화 정보 삭제
  def delete(self, title):
    if not title in movie_info.keys():
      abort(404, description=f"title {title} doesn't exists")
      
    del movie_info[title]
    return Response(status=200)


  # 영화 정보 변경
  def put(self, title):
    # todo
    return Response(status=200)
    

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
