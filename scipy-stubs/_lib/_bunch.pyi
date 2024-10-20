from typing import Any

def _validate_names(typename: str, field_names: list[str], extra_field_names: list[str]) -> None: ...
def _make_tuple_bunch(
    typename: str,
    field_names: list[str],
    extra_field_names: list[str] | None = None,
    module: str | None = None,
) -> type[tuple[Any, ...]]: ...
