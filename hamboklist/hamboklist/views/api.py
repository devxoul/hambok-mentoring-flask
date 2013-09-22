# -*- coding: utf-8 -*-

from flask import Blueprint, request, Response, abort, session
from hamboklist.model import *
from hamboklist.app import app
import json

api = Blueprint('api', __name__)

def json_response(obj={}):
	return Response(json.dumps(obj), mimetype='application/json')


def error(status_code, description):
	response = json_response({'error': {'description': description}})
	response.status_code = status_code
	abort(response)


def logged_in_user():
	user_id = session.get('user_id') or error(403, 'Not authorized.')
	user = User.query.filter(User.id == user_id).first() or error(403, 'Not authorized.')
	return user


@api.route('/')
def index():
	return json_response({
		'api': {
			'version': '1.0'
		}
	})


#
# User
#

@api.route('/login', methods=['POST'])
def login():
	email = request.form.get('email') or error(400, 'Need an email.')
	password = request.form.get('password') or error(400, 'Need a password.')
	user = User.query.filter(User.email == email).first() or error(404, 'No such user.')
	user = User.query.filter(User.email == email).filter(User.password == password).first() or error(400, 'Wrong password.')
	session['user_id'] = user.id
	return json_response(user.dictify()), 201


@api.route('/logout', methods=['GET'])
def logout():
	logged_in_user()
	session.pop('user_id')
	return json_response()


@api.route('/user', methods=['POST'])
def post_user():
	email = request.form.get('email') or error(400, 'Need an email.')
	password = request.form.get('password') or error(400, 'Need a password.')
	name = request.form.get('name')

	user = not User.query.filter(User.email == email).first() or error(400, 'Already signed up.')
	user = User()
	user.email = email
	user.password = password
	user.name = name

	db.session.add(user)
	db.session.commit()

	session['user_id'] = user.id

	return json_response(user.dictify()), 201


@api.route('/user', methods=['GET'])
def get_user(user_id):
	user = logged_in_user()
	return json_response(user.dictify())


@api.route('/user', methods=['PUT'])
def put_user(user_id):
	user = logged_in_user()
	
	email = request.form.get('email')
	password = request.form.get('password')
	name = request.form.get('name')

	if not email and not password and not name: error(400, 'Need at least one parameter.')
	if email: user.email = email
	if password: user.password = password
	if name: user.name = name

	db.session.add(user)
	db.session.commit()

	return json_response(user.dictify())


@api.route('/user', methods=['DELETE'])
def delete_user(user_id):
	user = logged_in_user()
	db.session.delete(user)
	db.session.commit()
	return json_response()


#
# List
#

@api.route('/lists', methods=['GET'])
def get_lists():
	user = logged_in_user()
	lists = {
		'lists': [list.dictify() for list in user.lists]
	}
	return json_response(lists)


@api.route('/list/<int:list_id>', methods=['GET'])
def get_list(list_id):
	user = logged_in_user()
	list = List.query.filter(List.id == list_id).filter(List.user_id == user.id).first() or error(404, 'No such list.')
	return json_response(list.dictify())


@api.route('/list', methods=['POST'])
def post_list():
	user = logged_in_user()
	name = request.form.get('name') or error(400, 'Need a name.')
	list = List()
	list.name = name
	list.user = user
	db.session.add(list)
	db.session.commit()
	return json_response(list.dictify()), 201

@api.route('/list/<int:list_id>', methods=['PUT'])
def put_list(list_id):
	user = logged_in_user()
	name = request.form.get('name') or error(400, 'Need a name.')
	list = List.query.filter(List.id == list_id).filter(List.user_id == user.id).first() or error(404, 'No such list.')
	list.name = name
	db.session.add(list)
	db.session.commit()
	return json_response(list.dictify())


@api.route('/list/<int:list_id>', methods=['DELETE'])
def delete_list(list_id):
	user = logged_in_user()
	list = List.query.filter(List.id == list_id).filter(List.user_id == user.id).first() or error(404, 'No such list.')
	db.session.delete(list)
	db.session.commit()
	return json_response()


#
# Task
#

@api.route('/list/<int:list_id>/task', methods=['POST'])
def post_list_task(list_id):
	user = logged_in_user()
	list = List.query.filter(List.id == list_id).filter(List.user_id == user.id).first() or error(404, 'No such list.')

	title = request.form.get('title') or error(400, 'Need a title.')
	description = request.form.get('description')

	task = Task()
	task.title = title
	task.description = description
	task.list = list
	task.user = user

	db.session.add(task)
	db.session.commit()

	return json_response(task.dictify()), 201


@api.route('/task/<int:task_id>', methods=['PUT'])
def put_task(task_id):
	user = logged_in_user()
	task = Task.query.filter(Task.id == task_id).filter(Task.user_id == user.id).first() or error(404, 'No such task.')

	title = request.form.get('title')
	description = request.form.get('description')
	complete = request.form.get('complete')
	list_id = request.form.get('list_id')
	if not title and not description and not complete and not list_id: error(400, 'Need at least one parameter.')
	if complete and complete != '0' and complete != '1': error(400, 'Parameter \'complete\' only accepts 0 or 1')

	if title: task.title = title
	if description: task.description = description
	if complete: task.complete = complete
	if list_id: task.list = List.query.filter(List.id == list_id).filter(List.user_id == user.id).first() or error(404, 'No such list.')

	db.session.add(task)
	db.session.commit()

	return json_response(task.dictify())


@api.route('/task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
	user = logged_in_user()
	task = Task.query.filter(Task.id == task_id).filter(Task.user_id == user.id).first() or error(404, 'No such task.')
	db.session.delete(task)
	db.session.commit()
	return json_response()

