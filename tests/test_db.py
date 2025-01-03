import sqlite3
import pytest
from recipe_db.db import get_db
"""
def test_get_recipe():
    response = db.db_get_recipes()
    print(response)
    assert "curry" in response
    assert "gnocchi" in response

def test_get_user():
    user = {"name": "test", "password": "test", "email": "test"}
    response = db.add_user(user)
    print(response)
    """


def test_get_close_db(app):
    with app.app_context():
        db = get_db()
        assert db is get_db()

    with pytest.raises(sqlite3.ProgrammingError) as e:
        db.execute('SELECT 1')

    assert 'closed' in str(e.value)

def test_init_db_command(runner, monkeypatch):
    class Recorder(object):
        called = False

    def fake_init_db():
        Recorder.called = True

    monkeypatch.setattr('app.db.init_db', fake_init_db)
    result = runner.invoke(args=['init-db'])
    assert 'Initialized' in result.output
    assert Recorder.called