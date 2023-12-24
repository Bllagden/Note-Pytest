"""Глобальный conftest.py
В каждой директории может быть свой локальный conftest.py.

conftest.py используется для хранения общих фикстур и настроек,
которые могут быть использованы в различных тестовых файлах.

Фикстуры, определенные в conftest.py, автоматически обнаруживаются pytest
и могут быть использованы в любом тесте без необходимости их импортировать.
"""

import pytest

from db import candies_model  # noqa: F401 (модели тоже нужно импортировать)
from db import Base, engine
from settings import db_settings


@pytest.fixture(scope="session", autouse=True)
def setup_db():
    """Применяется автоматически и только один раз в начале тестовой сессии.

    Есть два .env файла (.dev и .test), в них настройки для DEV-DB и для TEST-DB.
    При запуске тестов .env подменяется (с .dev на .test) библиотекой pytest-dotenv.

    Настройка в pyproject.toml:
        [tool.pytest.ini_options]
        env_files = [
            ".test.env",
        ]

    Проверка 'db_settings.MODE == "TEST"' не позволяет запустить тесты, если не .test.env.
    Ведь (.test.env: MODE=TEST), а (.dev.env: MODE=DEV)
    Таким образом в тестах используется только тестовая БД.

    Почему .dev.env (а не .env).
    Если запускать тесты из консоли, тогда pytest-dotenv позволяет выбрать .env файл:
        pytest --envfile .test.env -s -v
        pytest --envfile .test.env tests/unit_tests/test_candies_service.py -s -v

        флаг -s (для вывода принтов)
        флаг -v (для вывода подробностей)

    Но при запуске тестов из встроенного тест-раннера VScode, он не позволяет подменить
    .env файл на .test.env, и все равно использует .env при тестах (а там DEV-DB).
    При нейминге .dev.env вместо .env такой проблемы нет.
    """
    print("\nGlobal Fixture 'setup_db'")
    print("Begin setup")
    assert db_settings.MODE == "TEST"
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print("End setup")
    #
    # Base.metadata.drop_all(engine)
    # Base.metadata.create_all(engine)
    # yield  # отдача управления pytest-у (выполняются все тесты)
    # Base.metadata.drop_all(engine)
