# ruff: noqa: PYI042

# TODO: overloads for specific scalar-types (mind the int/float/complex promotion)
# TODO: pass the literal shape sizes to the shape parameters of the `_zeroes` return types (i.e. 1d arrays)

from typing import Any, Literal, TypeAlias, overload
from typing_extensions import TypeVar

import numpy as np
import numpy.typing as npt
import optype as op
import optype.numpy as onp
from numpy._typing import _ArrayLikeComplex_co, _ArrayLikeFloat_co, _ArrayLikeInt_co  # don't try this at home, kids
from ._ufuncs import psi as digamma  # completely different greek letters, but oh well...

__all__ = [
    "ai_zeros",
    "assoc_laguerre",
    "bei_zeros",
    "beip_zeros",
    "ber_zeros",
    "bernoulli",
    "berp_zeros",
    "bi_zeros",
    "clpmn",
    "comb",
    "digamma",
    "diric",
    "erf_zeros",
    "euler",
    "factorial",
    "factorial2",
    "factorialk",
    "fresnel_zeros",
    "fresnelc_zeros",
    "fresnels_zeros",
    "h1vp",
    "h2vp",
    "ivp",
    "jn_zeros",
    "jnjnp_zeros",
    "jnp_zeros",
    "jnyn_zeros",
    "jvp",
    "kei_zeros",
    "keip_zeros",
    "kelvin_zeros",
    "ker_zeros",
    "kerp_zeros",
    "kvp",
    "lmbda",
    "lpmn",
    "lpn",
    "lqmn",
    "lqn",
    "mathieu_even_coef",
    "mathieu_odd_coef",
    "obl_cv_seq",
    "pbdn_seq",
    "pbdv_seq",
    "pbvv_seq",
    "perm",
    "polygamma",
    "pro_cv_seq",
    "riccati_jn",
    "riccati_yn",
    "sinc",
    "stirling2",
    "y0_zeros",
    "y1_zeros",
    "y1p_zeros",
    "yn_zeros",
    "ynp_zeros",
    "yvp",
    "zeta",
]

_T0 = TypeVar("_T0")
_T1 = TypeVar("_T1")
_tuple2: TypeAlias = tuple[_T0, _T0]
_tuple4: TypeAlias = tuple[_T0, _T1, _T1, _T1]
_tuple8: TypeAlias = tuple[_T0, _T1, _T1, _T1, _T1, _T1, _T1, _T1]

_ArrayT = TypeVar("_ArrayT", bound=onp.Array)
_SCT = TypeVar("_SCT", bound=np.generic)
_SCT_fc = TypeVar("_SCT_fc", bound=np.inexact[Any])
_scalar_or_array: TypeAlias = _SCT | onp.ArrayND[_SCT]
_array_0d: TypeAlias = onp.Array[tuple[()], _SCT]
_array_1d: TypeAlias = onp.Array1D[_SCT]
_array_2d: TypeAlias = onp.Array2D[_SCT]
_array: TypeAlias = onp.ArrayND[_SCT]

_i1: TypeAlias = np.int8
_i2: TypeAlias = np.int16
_i4: TypeAlias = np.int32
_i8: TypeAlias = np.int64
_i: TypeAlias = _i1 | _i2 | _i4 | _i8

_f2: TypeAlias = np.float16
_f4: TypeAlias = np.float32
_f8: TypeAlias = np.float64
_f: TypeAlias = _f2 | _f4 | _f8 | np.longdouble

_c8: TypeAlias = np.complex64
_c16: TypeAlias = np.complex128
_c: TypeAlias = _c8 | _c16 | np.clongdouble

@overload
def sinc(x: np.integer[Any] | np.bool_) -> np.float64: ...
@overload
def sinc(x: _SCT_fc) -> _SCT_fc: ...
@overload
def sinc(x: npt.NDArray[np.integer[Any] | np.bool_]) -> npt.NDArray[np.float64]: ...
@overload
def sinc(x: npt.NDArray[_SCT_fc]) -> npt.NDArray[_SCT_fc]: ...
@overload
def sinc(x: _ArrayLikeFloat_co) -> np.floating[Any] | npt.NDArray[np.floating[Any]]: ...
@overload
def sinc(x: _ArrayLikeComplex_co) -> np.inexact[Any] | npt.NDArray[np.inexact[Any]]: ...
def diric(x: _ArrayLikeFloat_co, n: onp.ToInt) -> npt.NDArray[np.floating[Any]]: ...
def jnjnp_zeros(nt: onp.ToInt) -> _tuple4[_array_1d[_f8], _array_1d[_i4]]: ...
def jnyn_zeros(n: onp.ToInt, nt: onp.ToInt) -> _tuple4[_array_1d[_f8], _array_1d[_f8]]: ...
def jn_zeros(n: onp.ToInt, nt: onp.ToInt) -> _array_1d[_f8]: ...
def jnp_zeros(n: onp.ToInt, nt: onp.ToInt) -> _array_1d[_f8]: ...
def yn_zeros(n: onp.ToInt, nt: onp.ToInt) -> _array_1d[_f8]: ...
def ynp_zeros(n: onp.ToInt, nt: onp.ToInt) -> _array_1d[_f8]: ...
def y0_zeros(nt: onp.ToInt, complex: op.CanBool = False) -> _tuple2[_array_1d[_c16]]: ...
def y1_zeros(nt: onp.ToInt, complex: op.CanBool = False) -> _tuple2[_array_1d[_c16]]: ...
def y1p_zeros(nt: onp.ToInt, complex: op.CanBool = False) -> _tuple2[_array_1d[_c16]]: ...
def jvp(v: _ArrayLikeFloat_co, z: onp.ToComplex, n: onp.ToInt = 1) -> _scalar_or_array[_f4 | _f8 | _c8 | _c16]: ...
def yvp(v: _ArrayLikeFloat_co, z: onp.ToComplex, n: onp.ToInt = 1) -> _scalar_or_array[_f4 | _f8 | _c8 | _c16]: ...
def kvp(v: _ArrayLikeFloat_co, z: onp.ToComplex, n: onp.ToInt = 1) -> _scalar_or_array[_f4 | _f8 | _c8 | _c16]: ...
def ivp(v: _ArrayLikeFloat_co, z: onp.ToComplex, n: onp.ToInt = 1) -> _scalar_or_array[_f4 | _f8 | _c8 | _c16]: ...
def h1vp(v: _ArrayLikeFloat_co, z: onp.ToComplex, n: onp.ToInt = 1) -> _scalar_or_array[_f4 | _f8 | _c8 | _c16]: ...
def h2vp(v: _ArrayLikeFloat_co, z: onp.ToComplex, n: onp.ToInt = 1) -> _scalar_or_array[_f4 | _f8 | _c8 | _c16]: ...
def riccati_jn(n: onp.ToInt, x: onp.ToFloat) -> _tuple2[_array_1d[_f8]]: ...
def riccati_yn(n: onp.ToInt, x: onp.ToFloat) -> _tuple2[_array_1d[_f8]]: ...
def erf_zeros(nt: onp.ToInt) -> _array_1d[_c16]: ...
def fresnelc_zeros(nt: onp.ToInt) -> _array_1d[_c16]: ...
def fresnels_zeros(nt: onp.ToInt) -> _array_1d[_c16]: ...
def fresnel_zeros(nt: onp.ToInt) -> _array_1d[_c16]: ...
def assoc_laguerre(x: _ArrayLikeComplex_co, n: onp.ToInt, k: onp.ToFloat = 0.0) -> _scalar_or_array[_f4 | _f8 | _c8 | _c16]: ...
def polygamma(n: _ArrayLikeInt_co, x: _ArrayLikeFloat_co) -> _scalar_or_array[_f8]: ...
def mathieu_even_coef(m: onp.ToInt, q: onp.ToFloat) -> _array_1d[_f8]: ...
def mathieu_odd_coef(m: onp.ToInt, q: onp.ToFloat) -> _array_1d[_f8]: ...
def lpmn(m: onp.ToInt, n: onp.ToInt, z: _ArrayLikeFloat_co) -> _tuple2[_array_2d[_f8]]: ...
def clpmn(m: onp.ToInt, n: onp.ToInt, z: _ArrayLikeComplex_co, type: Literal[2, 3] = 3) -> _tuple2[_array_2d[_c16]]: ...
def lqmn(m: onp.ToInt, n: onp.ToInt, z: _ArrayLikeFloat_co) -> _tuple2[_array_2d[_f]] | _tuple2[_array_2d[_c]]: ...
def bernoulli(n: onp.ToInt) -> _array_1d[_f8]: ...
def euler(n: onp.ToInt) -> _array_1d[_f8]: ...
def lpn(n: onp.ToInt, z: onp.ToFloat) -> _tuple2[_array_1d[_f]] | _tuple2[_array_1d[_c]]: ...  # the dtype propagates
def lqn(n: onp.ToInt, z: npt.ArrayLike) -> _tuple2[_array_1d[_f8]] | _tuple2[_array_1d[_c16]]: ...  # either f8 or c16
def ai_zeros(nt: onp.ToInt) -> _tuple4[_array_1d[_f8], _array_1d[_f8]]: ...
def bi_zeros(nt: onp.ToInt) -> _tuple4[_array_1d[_f8], _array_1d[_f8]]: ...
def lmbda(v: onp.ToFloat, x: onp.ToFloat) -> _tuple2[_array_1d[_f8]]: ...
def pbdv_seq(v: onp.ToFloat, x: onp.ToFloat) -> _tuple2[_array_1d[_f8]]: ...
def pbvv_seq(v: onp.ToFloat, x: onp.ToFloat) -> _tuple2[_array_1d[_f8]]: ...
def pbdn_seq(n: onp.ToInt, z: onp.ToComplex) -> _tuple2[_array_1d[_c16]]: ...
def ber_zeros(nt: onp.ToInt) -> _array_1d[_f8]: ...
def bei_zeros(nt: onp.ToInt) -> _array_1d[_f8]: ...
def ker_zeros(nt: onp.ToInt) -> _array_1d[_f8]: ...
def kei_zeros(nt: onp.ToInt) -> _array_1d[_f8]: ...
def berp_zeros(nt: onp.ToInt) -> _array_1d[_f8]: ...
def beip_zeros(nt: onp.ToInt) -> _array_1d[_f8]: ...
def kerp_zeros(nt: onp.ToInt) -> _array_1d[_f8]: ...
def keip_zeros(nt: onp.ToInt) -> _array_1d[_f8]: ...
def kelvin_zeros(nt: onp.ToInt) -> _tuple8[_array_1d[_f8], _array_1d[_f8]]: ...
def pro_cv_seq(m: onp.ToInt, n: onp.ToInt, c: onp.ToFloat) -> _array_1d[_f8]: ...
def obl_cv_seq(m: onp.ToInt, n: onp.ToInt, c: onp.ToFloat) -> _array_1d[_f8]: ...
@overload
def comb(
    N: onp.ToInt | _array_0d[_i],
    k: onp.ToInt | _array_0d[_i],
    *,
    exact: Literal[True, 1],
    repetition: op.CanBool = False,
) -> int: ...
@overload
def comb(
    N: _ArrayLikeFloat_co,
    k: _ArrayLikeFloat_co,
    *,
    exact: Literal[False, 0] = False,
    repetition: op.CanBool = False,
) -> _scalar_or_array[_f4 | _f8]: ...
@overload
def perm(N: onp.ToInt | _array_0d[_i], k: onp.ToInt | _array_0d[_i], exact: Literal[True, 1]) -> int: ...
@overload
def perm(
    N: _ArrayLikeFloat_co,
    k: _ArrayLikeFloat_co,
    exact: Literal[False, 0] | None = False,
) -> _scalar_or_array[_f4 | _f8]: ...
@overload
def factorial(n: _ArrayLikeInt_co, exact: Literal[True, 1]) -> int | _array[np.int_]: ...
@overload
def factorial(n: _ArrayLikeFloat_co, exact: Literal[False, 0] | None = False) -> _scalar_or_array[_f8]: ...
@overload
def factorial2(n: _ArrayLikeInt_co, exact: Literal[True, 1]) -> _i | _array[np.int_]: ...
@overload
def factorial2(n: _ArrayLikeInt_co, exact: Literal[False, 0] | None = False) -> _scalar_or_array[_f8]: ...
@overload
def factorialk(n: _ArrayLikeInt_co, k: int | _i, exact: Literal[True, 1]) -> _i | _array[np.int_]: ...
@overload
def factorialk(n: _ArrayLikeInt_co, k: int | _i, exact: Literal[False, 0] | None = ...) -> _scalar_or_array[_f8]: ...
@overload
def stirling2(N: _ArrayLikeInt_co, K: _ArrayLikeInt_co, *, exact: Literal[True, 1]) -> int | _array[np.object_]: ...
@overload
def stirling2(N: _ArrayLikeInt_co, K: _ArrayLikeInt_co, *, exact: Literal[False, 0] | None = False) -> _scalar_or_array[_f8]: ...
@overload
def zeta(x: _ArrayLikeFloat_co, q: _ArrayLikeFloat_co | None, out: _ArrayT) -> _ArrayT: ...
@overload
def zeta(x: _ArrayLikeFloat_co, q: _ArrayLikeFloat_co | None = None, *, out: _ArrayT) -> _ArrayT: ...
@overload
def zeta(x: _ArrayLikeFloat_co, q: _ArrayLikeFloat_co | None = None, out: None = None) -> _scalar_or_array[_f8]: ...
