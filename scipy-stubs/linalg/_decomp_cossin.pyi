from typing import Any, Literal, TypeAlias, overload

import numpy as np
import numpy.typing as npt
import optype as op
import optype.numpy as onp
import optype.typing as opt

__all__ = ["cossin"]

_Array_f_1d: TypeAlias = onp.Array1D[np.floating[Any]]
_Array_f_2d: TypeAlias = onp.Array2D[np.floating[Any]]
_Array_c_2d: TypeAlias = onp.Array2D[np.complexfloating[Any, Any]]

@overload
def cossin(
    X: npt.ArrayLike | op.CanIter[op.CanNext[npt.ArrayLike]],
    p: opt.AnyInt | None = None,
    q: opt.AnyInt | None = None,
    separate: Literal[False] = False,
    swap_sign: bool = False,
    compute_u: bool = True,
    compute_vh: bool = True,
) -> tuple[_Array_f_2d, _Array_f_2d, _Array_f_2d] | tuple[_Array_c_2d, _Array_f_2d, _Array_c_2d]: ...
@overload
def cossin(
    X: npt.ArrayLike | op.CanIter[op.CanNext[npt.ArrayLike]],
    p: opt.AnyInt | None = None,
    q: opt.AnyInt | None = None,
    *,
    separate: Literal[True],
    swap_sign: bool = False,
    compute_u: bool = True,
    compute_vh: bool = True,
) -> (
    tuple[tuple[_Array_f_2d, _Array_f_2d], _Array_f_1d, tuple[_Array_f_2d, _Array_f_2d]]
    | tuple[tuple[_Array_c_2d, _Array_c_2d], _Array_f_1d, tuple[_Array_c_2d, _Array_c_2d]]
): ...
