import abc
import re
from csv import Dialect
from collections.abc import Iterable, Iterator, Sequence
from typing import Any, ClassVar, Final, Generic, Literal
from typing_extensions import Self, TypeVar

import numpy as np
import numpy.typing as npt
from scipy._typing import FileLike, FileName

__all__ = ["ArffError", "MetaData", "ParseArffError", "loadarff"]

_T_co = TypeVar("_T_co", covariant=True, default=object)

r_meta: re.Pattern[str]
r_comment: re.Pattern[str]
r_empty: re.Pattern[str]
r_headerline: re.Pattern[str]
r_datameta: re.Pattern[str]
r_relation: re.Pattern[str]
r_attribute: re.Pattern[str]
r_nominal: re.Pattern[str]
r_date: re.Pattern[str]
r_comattrval: re.Pattern[str]
r_wcomattrval: re.Pattern[str]

class ArffError(OSError): ...
class ParseArffError(ArffError): ...

class Attribute(Generic[_T_co], metaclass=abc.ABCMeta):
    type_name: ClassVar[Any]
    dtype: Any
    range: Any

    name: Final[str]

    def __init__(self, /, name: str) -> None: ...
    @classmethod
    def parse_attribute(cls, name: str, attr_string: str) -> Self | None: ...
    def parse_data(self, /, data_str: str) -> _T_co: ...

class NominalAttribute(Attribute[str]):
    type_name: ClassVar = "nominal"
    dtype: tuple[type[np.bytes_], ...]
    range: Sequence[str]

    values: Final[Sequence[str]]

    def __init__(self, /, name: str, values: Sequence[str]) -> None: ...

class NumericAttribute(Attribute[float]):
    type_name: ClassVar = "numeric"
    dtype: type[np.float64]
    range: None

class StringAttribute(Attribute[None]):
    type_name: ClassVar = "string"
    dtype: type[np.object_]
    range: None

class DateAttribute(Attribute[np.datetime64]):
    type_name: ClassVar = "date"
    dtype: np.datetime64
    range: str

    date_format: Final[str]
    datetime_unit: Final[str]

    def __init__(self, /, name: str, date_format: str, datetime_unit: str) -> None: ...

class RelationalAttribute(Attribute[np.ndarray[tuple[int], np.dtypes.VoidDType[int]]]):
    type_name: ClassVar = "relational"
    dtype: type[np.object_]
    range: None

    attributes: Final[list[Attribute]]
    dialect: Dialect | None

class MetaData:
    name: Final[str]
    def __init__(self, /, rel: str, attr: Iterable[Attribute]) -> None: ...
    def __iter__(self, /) -> Iterator[str]: ...
    def __getitem__(self, /, key: str) -> tuple[str, str | Sequence[str] | None]: ...
    def names(self, /) -> list[str]: ...
    def types(self, /) -> list[str]: ...

def to_attribute(name: str, attr_string: str) -> Attribute: ...
def csv_sniffer_has_bug_last_field() -> Literal[False]: ...
def workaround_csv_sniffer_bug_last_field(sniff_line: str, dialect: Dialect, delimiters: Iterable[str]) -> None: ...
def split_data_line(line: str, dialect: Dialect | None = None) -> tuple[list[str], Dialect]: ...
def tokenize_attribute(iterable: Iterable[int | str], attribute: str) -> tuple[Attribute, object]: ...
def tokenize_single_comma(val: str) -> tuple[str, str]: ...
def tokenize_single_wcomma(val: str) -> tuple[str, str]: ...
def read_relational_attribute(ofile: Iterator[str], relational_attribute: RelationalAttribute, i: str) -> str: ...
def read_header(ofile: Iterator[str]) -> tuple[str, list[Attribute]]: ...
def loadarff(f: FileLike[str]) -> tuple[npt.NDArray[np.void], MetaData]: ...
def basic_stats(data: npt.NDArray[np.number[Any]]) -> tuple[np.number[Any], np.number[Any], np.number[Any], np.number[Any]]: ...
def print_attribute(name: str, tp: Attribute, data: Any) -> None: ...
def test_weka(filename: FileName) -> None: ...
