from swadesh_list import app


@app.route('/about')
def about():
    return 'WOW'