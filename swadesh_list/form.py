from swadesh_list import app
from flask import abort, render_template
from flask_sqlalchemy import Pagination
import re
PER_PAGE = 10
FORM_ELEMS = 100


@app.route('/form', defaults={'page' : 1})
@app.route('/form/page/<int:page>')
def form(page):
    words = get_words_for_page(page, PER_PAGE, FORM_ELEMS)
    if page !=1:
        abort(404)
    pagination = Pagination(page, PER_PAGE,FORM_ELEMS)
    return render_template('form.html', pagination=pagination, words=words)


def get_words_for_page(page, per_page, count):
    list_of_words=get_swadesh_list()

    return None


def get_swadesh_list():
    with open('swadesh.txt', 'r') as t:
        lul = t.read().replace('#', '').replace('\t', '')
        swadesh_list = (re.sub(' ', '', lul).split('\n'))
    return swadesh_list