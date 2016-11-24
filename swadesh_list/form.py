from swadesh_list import app
from flask import abort, render_template, request, url_for
from flask_sqlalchemy import Pagination
from re import sub
from os.path import join, dirname, normpath
PER_PAGE = 10
FORM_ELEMS = 100


@app.route('/form/<int:page_num>')
def form(page_num):
    if request.args:
        print(request.args)
    print(page_num)
    # words = get_words_for_page(page_num, PER_PAGE, FORM_ELEMS)
    # if not words and page_num !=1:
    #     abort(404)
    # pagination = Pagination(page=page_num, per_page=PER_PAGE,total=FORM_ELEMS,)
    # words = "haha"
    # return render_template('form.html', pagination=pagination, words=words)
    words = get_words_for_page(page_num,PER_PAGE,FORM_ELEMS)
    # form_inp = SwadeshForm(request.form)
    print(words)
    if words == [] and page_num != 1:
        abort(404)
    return render_template('form.html', words=words)


def get_words_for_page(page_num, per_page, count):
    list_of_words=get_swadesh_list()
    first_word=(page_num-1)*per_page
    if first_word> count:
        per_page = None
    elif first_word + per_page > count:
        per_page= count - first_word
    page_words = list_of_words[first_word:first_word+per_page]
    return page_words
#
#
# def url_for_other_page(page):
#     url_args = request.view_args.copy()
#     url_args['page'] = page
#     return url_for(request.endpoint, **url_args)


def get_swadesh_list():
    with open(join(dirname(normpath(__file__)),'static','swadesh.txt'), 'r') as t:
        lul = t.read().replace('#', '').replace('\t', '')
        swadesh_list = (sub(' ', '', lul).split('\n'))
    return swadesh_list