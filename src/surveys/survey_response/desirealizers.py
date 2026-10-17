from collections.abc import Mapping
from dataclasses import dataclass
from typing import Literal, Union

from app_types.answer import AnswerType, AnswerTypeMapPType

ValueType = Union[list["ValueType"], Mapping[str, "ValueType"], str, int, float, bool]


@dataclass
class Answer:
    value: ValueType
    type: Literal[AnswerType.values]


@dataclass
class AnswersData:
    question_id: int
    answer: Answer
    user_id: int


@dataclass
class CreateData:
    survey_id: int
    answers: list[AnswersData]


def ensure_int(v: ValueType) -> int:
    if isinstance(v, int):
        return v
    else:
        raise TypeError(f"{v} not an integer")


def ensure_dict(v: ValueType) -> dict:
    if isinstance(v, dict):
        return v
    else:
        raise TypeError(f"{v} not an dictionary")

def deserialize_data_answer(v:ValueType, type: AnswerType) -> Answer:
    if not isinstance(v, AnswerTypeMapPType[type]):
        raise TypeError(f"{v} not an {AnswerTypeMapPType[type]}")
    return Answer(
        value=v,
        type=type,
    )

def deserialize_data(v: dict) -> CreateData:
    ensure_dict(v)

    return CreateData(
        survey_id=ensure_int(v["survey"]),
        answers=[
            AnswersData(
                question_id=ensure_int(item["question"]),
                answer=deserialize_data_answer(
                    v=item["value"],
                    type=AnswerType(item["type"])
                ),
                user_id=ensure_int(item["user_id"]),
            )
            for item in v["answers"]
        ],
    )
