from pydantic import BaseModel, ConfigDict, Field


class CandySchema(BaseModel):
    """candy_1 = CandySchema()
    or candy_2 = CandySchema(title="AAA", state="eaten", ...)"""

    id: int | None = Field(default=1)
    title: str = Field(default="Конфета")
    state: str = Field(default="full")
    owner: str = Field(default="teacher")

    model_config = ConfigDict(from_attributes=True)

    # Старый способ
    # class Config:
    #   from_attributes = True

    def __eq__(self, other) -> bool:
        """Проверка объектов на равенство (CandySchema_1 == CandySchema_2).
        Сравниваются поля объектов: ["title", "state", "owner"].

        Метод нужен для тестирования CandiesService.list().
        Там происходит поиск объекта CandySchema в list[CandySchema] оператором in.
        """
        if not isinstance(other, type(self)):
            return False
        for attr in ["title", "state", "owner"]:
            if getattr(self, attr) != getattr(other, attr):
                return False
        return True

    def to_dict_without_id(self) -> dict:
        """Генерирует dict представление модели.
        exclude={"id"} - исключить id из dict."""
        return self.model_dump(exclude={"id"})
