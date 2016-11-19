from flask import Flask
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


import swadesh_list.index
import swadesh_list.register
import swadesh_list.about
import swadesh_list.form
import swadesh_list.shortform
import swadesh_list.json_download_page
import swadesh_list.login
import swadesh_list.search
import swadesh_list.stats
# app.jinja_env.globals['url_for_other_page'] = swadesh_list.form.url_for_other_page
