from app import db 

class userLogin(db.Model):
   username=db.Column(db.String(20),primary_key=True)
   passwrd=db.Column(db.String(20))

   def __init__(self,username,passwrd):
      self.username=username
      self.passwrd=passwrd