from models.database import db 

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename  = db.Column(db.String(150), nullable = False)
    upload_time = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<File {self.filename}>'