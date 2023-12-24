import pytest

from candies import CandiesService, CandySchema


@pytest.mark.usefixtures("delete_all_candies")
class TestCandiesService:
    """Фикстуры из conftest.py:'delete_all_candies' и 'candies'.
    Импортировать их не нужно, pytest сам их распознает.

    Фикстура 'delete_all_candies' применятся ко всем тестам в классе (методам).
    При этом фикстуры можно передавать напрямую в функции, как фикстуру 'candies'.

    pytest --envfile .test.env tests/unit_tests/test_candies_service.py -s -v
    pytest --envfile .test.env tests/unit_tests/test_candies_service.py::TestCandiesService::test_count -s -v
    pytest --envfile .test.env tests/unit_tests/test_candies_service.py::TestCandiesService::test_list -s -v
        флаг -s (для вывода принтов)
        флаг -v (для вывода подробностей)
    """

    def test_count(self, candies):
        for candy in candies:
            CandiesService.add(candy)
        assert CandiesService.count() == len(candies)

    def test_list(self, candies):
        for candy in candies:
            CandiesService.add(candy)

        new_candies = CandiesService.list()
        for added_candy in new_candies:
            assert CandySchema(**added_candy) in candies
