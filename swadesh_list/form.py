from swadesh_list import app
from flask import abort, render_template, request, url_for
from flask_sqlalchemy import Pagination
import re
PER_PAGE = 10
FORM_ELEMS = 100


@app.route('/form', defaults={'page_num' : 1})
@app.route('/form/page/<int:page_num>')
def form(page_num):
    words = get_words_for_page(page_num, PER_PAGE, FORM_ELEMS)
    if not words and page_num !=1:
        abort(404)
    pagination = Pagination(page_num, PER_PAGE,FORM_ELEMS)
    words = "haha"
    return render_template('form.html', pagination=pagination, words=words)


def get_words_for_page(page_num, per_page, count):
    list_of_words=get_swadesh_list()
    first_word=page_num*(per_page-1)
    page_words = list_of_words[first_word:count-page_num]
    return None


def url_for_other_page(page):
    url_args = request.view_args.copy()
    url_args['page'] = page
    return url_for(request.endpoint, **url_args)


def get_swadesh_list():
    with open('\\static\\swadesh.txt', 'r') as t:
        lul = t.read().replace('#', '').replace('\t', '')
        swadesh_list = (re.sub(' ', '', lul).split('\n'))
    return swadesh_list