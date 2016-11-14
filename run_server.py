from database import db_session, init_db
from swadesh_list import app


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    init_db()
    app.run(debug=True)