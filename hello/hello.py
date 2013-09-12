# -*- coding: utf-8 -*-

from flask import Flask, request
import os

PORT = 5000

# 해당 port를 사용중인 프로세스 종료
os.system("lsof -i -P | awk '$9 ~ /:%d/ {print $2}' | xargs kill -9" % PORT)

app = Flask(__name__)

@app.route('/')
def index():
	return 'It Works!'

@app.route('/hello')
def hello():
	return 'Hello, World!'

@app.route('/user/<username>')
def get_user(username):
	return 'User %s' % username

@app.route('/post/<int:post_id>')
def get_post(post_id):
	return 'Post %d' % post_id

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return 'Show login form'

	elif request.method == 'POST':
		return 'Do login'

if __name__ == '__main__':
	app.run(port=PORT)