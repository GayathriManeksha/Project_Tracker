from app import db


class userLogin(db.Model):
    username = db.Column(db.String(20), primary_key=True)
    passwrd = db.Column(db.String(20))

    def __init__(self, username, passwrd):
        self.username = username
        self.passwrd = passwrd


class userDetails(db.Model):
    # id=db.Column('id',db.Integer,primary_key=True)
    username = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(20))
    address = db.Column(db.String(20))
    ph_no = db.Column(db.String(12))
    part = db.Column(db.String(20))

    def __init__(self, username, name, address, ph_no, part):
        self.username = username
        self.name = name
        self.address = address
        self.ph_no = ph_no
        self.part = part


class tasks(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column(db.String(20), db.ForeignKey(userLogin.username))
    task_desc = db.Column(db.String(20))
    status = db.Column(db.Integer)

    def __init__(self, username, task_desc):
        self.username = username
        self.task_desc = task_desc
        self.staus = 0
