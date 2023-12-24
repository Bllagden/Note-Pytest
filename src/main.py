import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], "src"))

from candies import CandiesRepository, CandiesService, CandySchema  # noqa: E402, F401
from db import Base, engine  # noqa: E402


def setup_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def add_candy(new_candy: CandySchema):
    added_candy = CandiesService.add(new_candy)
    print(f"{added_candy=}")


def get_candy(id: int):
    candy_by_id = CandiesService.get(id)
    print(f"{candy_by_id=}")


def get_all_candies():
    all_candies = CandiesService.list()
    print(f"{all_candies=}")


if __name__ == "__main__":
    print("\n", " Candies ".center(80, "="), sep="")
    setup_db()

    # a_dict = {"title": "sdfsdf"}
    # b_dict = {"title": "FDKJGKDFGL"}
    # a = CandiesRepository.add(a_dict)
    # b = CandiesRepository.add(b_dict)

    new_candy_1 = CandySchema(title="Сникерс")
    new_candy_2 = CandySchema(title="Баунти", state="full")
    new_candy_3 = CandySchema(title="Марс", state="half", owner="student")
    add_candy(new_candy_1)
    add_candy(new_candy_2)
    add_candy(new_candy_3)
    print()

    get_candy(3)
    get_candy(4)
    print()

    CandiesService.update(2, CandySchema(state="half"))
    CandiesService.finish(3)
    get_all_candies()
    print("Count:", CandiesService.count())
