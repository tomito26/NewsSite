from flask import render_template
from app import app

#views 
@app.route('/')
def index():
    '''
    View root page function that returns page and its data
    '''
    
    return render_template('index.html')
