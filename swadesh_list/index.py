from swadesh_list import app
from flask import request, render_template


@app.route('/')
def index():
    if request.method == 'POST':
        return 'LUL'
    return render_template('test.html')