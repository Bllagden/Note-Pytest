from pydantic import TypeAdapter

from .repository import CandiesRepository
from .schemas import CandySchema


class CandiesService:
    """TypeAdapter - класс для валидации и сериализации на основе типов Python.

    .dump_python - сериализует экземпляр адаптированного типа в объект Python."""

    @classmethod
    def add(cls, candy: CandySchema):
        """Добавляет конфету.
        Создается объект схемы, возвращается ее dict версия без id, передается в репо.
        Из репо возвращается scalar-объект и сериализуется в dict."""
        candy_dict = candy.to_dict_without_id()  # dict
        new_candy = CandiesRepository.add(candy_dict)  # <db.candies_model.Candies>

        # т.к. new_candy scalar-объект, результат словаря неупорядочен.
        # (видимо .dump_python использует set для дампа из scalar-объектов).
        # с RowMapping таких проблем нет.
        return TypeAdapter(CandySchema).dump_python(new_candy)

    @classmethod
    def get(cls, candy_id: int) -> dict | None:
        """Без преобразования RowMapping в CandySchema - Pydantic serializer warnings:
        Expected `CandySchema` but got `RowMapping` - serialized value may not be as expected
        """
        candy = CandiesRepository.get(candy_id)
        if candy:
            candy = CandySchema(**candy)  # преобразование RowMapping в CandySchema
        return TypeAdapter(CandySchema).dump_python(candy)

    @classmethod
    def list(
        cls,
        title: str | None = None,
        state: str | None = None,
        owner: str | None = None,
    ) -> list[dict]:
        """Передает в CandiesRepository либо сконструированный словарь, либо пустой."""
        filter_by: dict = {
            k: v
            for k, v in {"title": title, "state": state, "owner": owner}.items()
            if v
        }
        candies = CandiesRepository.list(filter_by)  #  list[<db.candies_model.Candies>]

        # такая же проблема с неупорядоченностью ключей в словарях, как и в add.
        return TypeAdapter(list[CandySchema]).dump_python(candies)

    @classmethod
    def count(cls) -> int:
        """Возвращает количество конфет (количество id)."""
        count = CandiesRepository.count()
        return count

    @classmethod
    def update(cls, candy_id: int, candy: CandySchema):
        """1, CandySchema(title="OOO", ...)"""
        candy_dict = candy.to_dict_without_id()
        CandiesRepository.update(candy_id, candy_dict)

    @classmethod
    def finish(cls, candy_id: int):
        """Меняет состояние конфеты на съеденную."""
        finish_dict = {"state": "eaten"}
        CandiesRepository.update(candy_id, finish_dict)

    @classmethod
    def delete(cls, candy_id: int):
        """Удаляет одну конфету по id."""
        CandiesRepository.delete(candy_id)

    @classmethod
    def delete_all(cls):
        """Удаляет все конфеты (не таблицу)."""
        CandiesRepository.delete_all()
