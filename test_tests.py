import pytest
import app
import os.path

# что после вызова функции создания базы
# а) появляется база данных,
# б) база данных содержит необходимые колонки,
# в) в базе данных есть строки и их не менее 10-ти


def test_create_tables():
    app.create_tables()
    assert os.path.exists(app.name_db) == True

def test_contains_columns_clients():
    p1 = 'SELECT "t1"."id", "t1"."name", "t1"."city", "t1"."address" FROM "clients" AS "t1"'
    assert str(app.clients.select()) == p1

def test_contains_columns_orders():
    p2 = 'SELECT "t1"."id", "t1"."client_id", "t1"."date", "t1"."amount", "t1"."description" FROM "orders" AS "t1"'
    assert str(app.orders.select()) == p2

def test_fill_rows_clients():
    app.filling_tables()
    assert len(app.clients.select()) >= 10

def test_fill_rows_orders():
    assert len(app.orders.select()) >= 10