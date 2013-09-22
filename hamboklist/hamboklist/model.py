from database import db


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(40))
	email = db.Column(db.String(40), nullable=False)
	password = db.Column(db.String(160), nullable=False)
	lists = db.relationship('List', backref='user')
	tasks = db.relationship('Task', backref='user')

	def dictify(self):
		return {
			'id': self.id,
			'name': self.name,
			'email': self.email
		}


class List(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(40), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	tasks = db.relationship('Task', backref='list')

	def dictify(self):
		return {
			'id': self.id,
			'name': self.name,
			'tasks': [task.dictify() for task in self.tasks]
		}


class Task(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(40), nullable=False)
	description = db.Column(db.Text)
	complete = db.Column(db.Boolean, default=False, nullable=False)
	list_id = db.Column(db.Integer, db.ForeignKey('list.id'), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def dictify(self):
		return {
			'id': self.id,
			'title': self.title,
			'description': self.description,
			'complete': self.complete,
		}