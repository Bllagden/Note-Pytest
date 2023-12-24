"""Фикстуры - функции, которые настраивают данные или среду для тестов.
Создаются при первом запросе тестом и уничтожаются в зависимости от их области действия (scope).
Пока фикстура не уничтожена, она не может быть использована снова.

1. function: (по умолчанию) Фикстура уничтожается в конце каждого теста, где она используется.
2. class: Фикстура уничтожается во время завершения последнего теста в классе.
3. module: Фикстура уничтожается после выполнения последнего теста в модуле.
4. package: фикстура уничтожается во время завершения последнего теста в пакете.
5. session: Фикстура уничтожается в конце тестовой сессии.
"""

import pytest

from candies import CandiesService, CandySchema


@pytest.fixture
def delete_all_candies():
    CandiesService.delete_all()


@pytest.fixture
def candies():
    cand = [
        CandySchema(title="candy_1"),
        CandySchema(title="candy_2", state="half"),
        CandySchema(title="candy_3", state="eaten"),
    ]
    return cand
