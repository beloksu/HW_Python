import pytest
from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    insert,
    update,
    delete,
    select
)
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql://postgres:ifkeey@localhost:5432/postgres'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
metadata = MetaData()

users_table = Table('users', metadata, autoload_with=engine)
subject_table = Table('subject', metadata, autoload_with=engine)
student_table = Table('student', metadata, autoload_with=engine)


@pytest.fixture(scope="module")
def db_session():
    yield session
    session.rollback()
    session.close()


def test_add_user(db_session):
    new_user = {
        'user_id': 9999,
        'user_email': 'test@example.com',
        'subject_id': 1
        }
    insert_stmt = insert(users_table).values(new_user)
    db_session.execute(insert_stmt)
    db_session.commit()

    query = select(users_table).where(users_table.c.user_id == 9999)
    result = db_session.execute(query).fetchone()
    assert result is not None
    assert result[1] == 'test@example.com'

    delete_stmt = delete(users_table).where(users_table.c.user_id == 9999)
    db_session.execute(delete_stmt)
    db_session.commit()


def test_update_user(db_session):
    db_session.execute(
        insert(users_table).values(
            {
                'user_id': 9999,
                'user_email': 'temp@example.com',
                'subject_id': 1
            }
        )
    )
    db_session.commit()

    update_stmt = update(users_table).where(
        users_table.c.user_id == 9999
    ).values(
        user_email='updated@example.com'
    )
    db_session.execute(update_stmt)
    db_session.commit()

    query = select(users_table).where(users_table.c.user_id == 9999)
    result = db_session.execute(query).fetchone()
    assert result[1] == 'updated@example.com'

    db_session.execute(
        delete(users_table).where(
            users_table.c.user_id == 9999
        )
    )
    db_session.commit()


def test_delete_user(db_session):
    db_session.execute(
        insert(users_table).values(
            {
                'user_id': 9999,
                'user_email': 'delete@example.com',
                'subject_id': 1
            }
        )
    )
    db_session.commit()

    delete_stmt = delete(users_table).where(users_table.c.user_id == 9999)
    db_session.execute(delete_stmt)
    db_session.commit()

    query = select(users_table).where(users_table.c.user_id == 9999)
    result = db_session.execute(query).fetchone()
    assert result is None
