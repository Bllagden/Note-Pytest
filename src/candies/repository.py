from sqlalchemy import delete, func, insert, select, update

from db import Candies, session_factory


class CandiesRepository:
    @classmethod
    def add(cls, values: dict):  # -> <db.candies_model.Candies>:
        """Добавляет новую конфету в БД, и возвращает ее как scalar-объект.
        К полям scalar-объекта можно обращаться: res.id; res.title; ...

        values = {"title": "AAA", "state": "full", "owner": "teacher"}"""
        with session_factory() as session:
            stmt = insert(Candies).values(**values).returning(Candies)
            # .returning() возвращает то, что вставлено в БД.

            new_candy = session.execute(stmt)  # <...ChunkedIteratorResult>
            session.commit()
            return new_candy.scalar_one()

    @classmethod
    def get(cls, candy_id: int):  # -> RowMapping | None:
        """Возвращает конфету из БД.

        mappings() преобразует результат запроса в RowMapping.
        Это тип результата, который позволяет извлекать строки в виде словарей."""
        query = select(Candies.__table__.columns).filter_by(id=candy_id)
        # print(candy)
        #   Candies.__table__.columns - <...CursorResult>
        #   print(res) - {'id': 1, 'title': 'sn', 'state': 'full', 'owner': 'teacher'}

        #   Candies - <...ChunkedIteratorResult>
        #   print(res) - {'Candies': <db.candies_model.Candies>}
        with session_factory() as session:
            candy = session.execute(query)
            session.commit()
            return candy.mappings().one_or_none()  # one()

    @classmethod
    def list(cls, filter_by: dict):  # -> list[<db.candies_model.Candies>]:
        """Возвращает список со всеми конфетами из БД.
        filter_by = {"title": "AAA", "state": "full", "owner": "teacher"} or {}"""
        query = select(Candies).filter_by(**filter_by)
        with session_factory() as session:
            candies = session.execute(query)
            session.commit()
            return candies.scalars().all()

    @classmethod
    def count(cls) -> int:
        """Возвращает количество конфет (количество id)."""
        query = select(func.count(Candies.id)).select_from(Candies)
        with session_factory() as session:
            candies_count = session.execute(query)
            session.commit()
            return candies_count.scalar()

    @classmethod
    def update(cls, candy_id: int, values: dict):
        """values = {"title": "AAA", "state": "bbb", "owner": "ccc"}"""
        stmt = update(Candies).where(Candies.id == candy_id).values(**values)
        with session_factory() as session:
            session.execute(stmt)
            session.commit()

    @classmethod
    def delete(cls, candy_id: int):
        """Удаляет одну конфету по id."""
        stmt = delete(Candies).where(Candies.id == candy_id)
        with session_factory() as session:
            session.execute(stmt)
            session.commit()

    @classmethod
    def delete_all(cls):
        """Удаляет все конфеты (не таблицу)."""
        stmt = delete(Candies)
        with session_factory() as session:
            session.execute(stmt)
            session.commit()
