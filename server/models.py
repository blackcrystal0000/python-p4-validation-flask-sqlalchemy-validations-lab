from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('name')
    def validates_name(self, key, name):
        if not name:
            raise ValueError("Please enter a name")
        return name
    
    @validates('phone_number')
    def validate_number(self, key, number):
        if len(number) != 10:
            raise ValueError("Please enter a valid phone number")
        return number

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('title')
    def validates_title(self, key, title):
        if not title:
            raise ValueError("Please enter a title")
        clickbait = ["Won't Believe", "Secret", "Top", "Guess"]
        if not any(substring in title for substring in clickbait):
            raise ValueError("Please include either of these phrases in the title: \n'Won't Believe' \n'Secret' \n'Top' \n'Guess'")
        return title
    
    @validates('content')
    def validate_content(self, key, content):
        if len(content) <= 250:
            raise ValueError("Content should contain atleast 250 characters")
        return content
    
    @validates('summary')
    def validate_summary(self, key, summary):
        if len(summary) >= 250:
            raise ValueError("Summary cannot exceed 250 characters")
        return summary
    
    @validates('category')
    def validate_category(self, key, category):
        if((category != 'Fiction') and (category != 'Non-Fiction')):
            raise ValueError("Category should be either Fiction or Non-Fiction.")
        return category

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'