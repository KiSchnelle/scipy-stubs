from dataclasses import dataclass
from collections.abc import Callable, Mapping, Sequence
from typing import Any, ClassVar, Generic, Literal, Protocol, TypeAlias, TypeVar, overload, type_check_only
from typing_extensions import deprecated

import numpy as np
import optype.numpy as onp
from scipy._typing import Alternative, ToRNG
from ._common import ConfidenceInterval

__all__ = ["bootstrap", "monte_carlo_test", "permutation_test"]

_FloatND: TypeAlias = float | np.float64 | onp.Array[Any, np.float64]
_FloatNDT_co = TypeVar("_FloatNDT_co", bound=_FloatND, default=_FloatND, covariant=True)

_BootstrapMethod: TypeAlias = Literal["percentile", "basic", "bca", "BCa"]
_PermutationType: TypeAlias = Literal["independent", "samples", "pairings"]

_Statistic: TypeAlias = Callable[..., onp.ToFloat] | Callable[..., onp.ToFloatND]

@type_check_only
class _RVSCallable(Protocol):
    def __call__(self, /, *, size: tuple[int, ...]) -> onp.ArrayND[np.floating[Any]]: ...

###

@dataclass
class PowerResult(Generic[_FloatNDT_co]):
    power: _FloatNDT_co
    pvalues: _FloatNDT_co

@dataclass
class BootstrapResult(Generic[_FloatNDT_co]):
    confidence_interval: ConfidenceInterval
    bootstrap_distribution: onp.ArrayND[np.float64]
    standard_error: _FloatNDT_co

@dataclass
class PermutationTestResult(Generic[_FloatNDT_co]):
    statistic: _FloatNDT_co
    pvalue: _FloatNDT_co
    null_distribution: onp.ArrayND[np.float64]

@dataclass
class MonteCarloTestResult(Generic[_FloatNDT_co]):
    statistic: _FloatNDT_co
    pvalue: _FloatNDT_co
    null_distribution: onp.ArrayND[np.float64]

@dataclass
class ResamplingMethod:
    n_resamples: int = 9_999
    batch: int | None = None

@dataclass
class MonteCarloMethod(ResamplingMethod):
    rvs: _RVSCallable | Sequence[_RVSCallable] | None = None
    rng: ToRNG = None

    def __init__(
        self,
        n_resamples: int = 9_999,
        batch: int | None = None,
        rvs: _RVSCallable | Sequence[_RVSCallable] | None = None,
        rng: ToRNG = None,
    ) -> None: ...

@dataclass
class PermutationMethod(ResamplingMethod):
    # this is a workaround for the horrible way in which `rng` is declared at runtime
    __match_args__: ClassVar[tuple[str, ...]] = "n_resamples", "batch", "rng"  # pyright: ignore[reportIncompatibleVariableOverride]

    @property
    def rng(self, /) -> ToRNG: ...
    #
    @property
    def random_state(self, /) -> ToRNG: ...
    @random_state.setter
    def random_state(self, rng: ToRNG, /) -> None: ...
    #
    @overload
    def __init__(
        self,
        n_resamples: int = 9_999,
        batch: int | None = None,
        random_state: None = None,
        *,
        rng: ToRNG = None,
    ) -> None: ...
    @overload
    @deprecated("`random_state` is deprecated, use `rng` instead")  # this is a reasonable lie
    def __init__(self, n_resamples: int, batch: int | None, random_state: ToRNG, *, rng: ToRNG = None) -> None: ...
    @overload
    @deprecated("`random_state` is deprecated, use `rng` instead")  # this is a reasonable lie
    def __init__(self, n_resamples: int = 9_999, batch: int | None = None, *, random_state: ToRNG, rng: ToRNG = None) -> None: ...

@dataclass(match_args=False)
class BootstrapMethod(ResamplingMethod):
    # this is a workaround for the horrible way in which `rng` is declared at runtime
    __match_args__: ClassVar[tuple[str, ...]] = "n_resamples", "batch", "rng", "method"  # pyright: ignore[reportIncompatibleVariableOverride]

    method: _BootstrapMethod = "BCa"

    @property
    def rng(self, /) -> ToRNG: ...
    #
    @property
    def random_state(self, /) -> ToRNG: ...
    @random_state.setter
    def random_state(self, rng: ToRNG, /) -> None: ...
    #
    @overload
    def __init__(
        self,
        /,
        n_resamples: int = 9_999,
        batch: int | None = None,
        random_state: None = None,
        method: _BootstrapMethod = "BCa",
        *,
        rng: ToRNG = None,
    ) -> None: ...
    @overload
    @deprecated("`random_state` is deprecated, use `rng` instead")  # this is a reasonable lie
    def __init__(
        self,
        /,
        n_resamples: int,
        batch: int | None,
        method: _BootstrapMethod,
        random_state: ToRNG,
        *,
        rng: ToRNG = None,
    ) -> None: ...
    @overload
    @deprecated("`random_state` is deprecated, use `rng` instead")  # this is a reasonable lie
    def __init__(
        self,
        /,
        n_resamples: int = 9_999,
        batch: int | None = None,
        method: _BootstrapMethod = "BCa",
        *,
        random_state: ToRNG,
        rng: ToRNG = None,
    ) -> None: ...

#
def power(
    test: _Statistic,
    rvs: _RVSCallable,
    n_observations: onp.ToJustInt1D | onp.ToJustInt2D,
    *,
    significance: onp.ToFloat | onp.ToFloatND = 0.01,
    kwargs: Mapping[str, object] | None = None,
    vectorized: bool | None = None,
    n_resamples: int = 10_000,
    batch: int | None = None,
) -> PowerResult: ...  # undocumented

###

#
@overload
def bootstrap(
    data: onp.ToFloatStrict1D,
    statistic: _Statistic,
    *,
    n_resamples: int = 9_999,
    batch: int | None = None,
    vectorized: bool | None = None,
    paired: bool = False,
    axis: Literal[0, -1] = 0,
    confidence_level: float = 0.95,
    alternative: Alternative = "two-sided",
    method: _BootstrapMethod = "BCa",
    bootstrap_result: BootstrapResult | None = None,
    rng: ToRNG = None,
) -> BootstrapResult[float | np.float64]: ...
@overload
def bootstrap(
    data: onp.ToFloatStrict2D,
    statistic: _Statistic,
    *,
    n_resamples: int = 9_999,
    batch: int | None = None,
    vectorized: bool | None = None,
    paired: bool = False,
    axis: Literal[0, 1, -1, -2] = 0,
    confidence_level: float = 0.95,
    alternative: Alternative = "two-sided",
    method: _BootstrapMethod = "BCa",
    bootstrap_result: BootstrapResult | None = None,
    rng: ToRNG = None,
) -> BootstrapResult[onp.Array1D[np.float64]]: ...
@overload
def bootstrap(
    data: onp.ToFloatStrict3D,
    statistic: _Statistic,
    *,
    n_resamples: int = 9_999,
    batch: int | None = None,
    vectorized: bool | None = None,
    paired: bool = False,
    axis: Literal[0, 1, 2, -1, -2, -3] = 0,
    confidence_level: float = 0.95,
    alternative: Alternative = "two-sided",
    method: _BootstrapMethod = "BCa",
    bootstrap_result: BootstrapResult | None = None,
    rng: ToRNG = None,
) -> BootstrapResult[onp.Array2D[np.float64]]: ...
@overload
def bootstrap(
    data: onp.ToFloatND,
    statistic: _Statistic,
    *,
    n_resamples: int = 9_999,
    batch: int | None = None,
    vectorized: bool | None = None,
    paired: bool = False,
    axis: int = 0,
    confidence_level: float = 0.95,
    alternative: Alternative = "two-sided",
    method: _BootstrapMethod = "BCa",
    bootstrap_result: BootstrapResult | None = None,
    rng: ToRNG = None,
) -> BootstrapResult: ...

#
@overload
def permutation_test(
    data: onp.ToFloatStrict1D,
    statistic: _Statistic,
    *,
    permutation_type: _PermutationType = "independent",
    vectorized: bool | None = None,
    n_resamples: int = 9_999,
    batch: int | None = None,
    alternative: Alternative = "two-sided",
    axis: Literal[0, -1] = 0,
    rng: ToRNG = None,
) -> PermutationTestResult[float | np.float64]: ...
@overload
def permutation_test(
    data: onp.ToFloatStrict2D,
    statistic: _Statistic,
    *,
    permutation_type: _PermutationType = "independent",
    vectorized: bool | None = None,
    n_resamples: int = 9_999,
    batch: int | None = None,
    alternative: Alternative = "two-sided",
    axis: Literal[0, 1, -1, -2] = 0,
    rng: ToRNG = None,
) -> PermutationTestResult[onp.Array1D[np.float64]]: ...
@overload
def permutation_test(
    data: onp.ToFloatStrict3D,
    statistic: _Statistic,
    *,
    permutation_type: _PermutationType = "independent",
    vectorized: bool | None = None,
    n_resamples: int = 9_999,
    batch: int | None = None,
    alternative: Alternative = "two-sided",
    axis: Literal[0, 1, 2, -1, -2, -3] = 0,
    rng: ToRNG = None,
) -> PermutationTestResult[onp.Array2D[np.float64]]: ...
@overload
def permutation_test(
    data: onp.ToFloatND,
    statistic: _Statistic,
    *,
    permutation_type: _PermutationType = "independent",
    vectorized: bool | None = None,
    n_resamples: int = 9_999,
    batch: int | None = None,
    alternative: Alternative = "two-sided",
    axis: int = 0,
    rng: ToRNG = None,
) -> PermutationTestResult: ...

#
@overload
def monte_carlo_test(
    data: onp.ToFloatStrict1D,
    rvs: _RVSCallable,
    statistic: _Statistic,
    *,
    vectorized: bool | None = None,
    n_resamples: int = 9_999,
    batch: int | None = None,
    alternative: Alternative = "two-sided",
    axis: Literal[0, -1] = 0,
) -> MonteCarloTestResult[float | np.float64]: ...
@overload
def monte_carlo_test(
    data: onp.ToFloatStrict2D,
    rvs: _RVSCallable,
    statistic: _Statistic,
    *,
    vectorized: bool | None = None,
    n_resamples: int = 9_999,
    batch: int | None = None,
    alternative: Alternative = "two-sided",
    axis: Literal[0, 1, -1, -2] = 0,
) -> MonteCarloTestResult[onp.Array1D[np.float64]]: ...
@overload
def monte_carlo_test(
    data: onp.ToFloatStrict3D,
    rvs: _RVSCallable,
    statistic: _Statistic,
    *,
    vectorized: bool | None = None,
    n_resamples: int = 9_999,
    batch: int | None = None,
    alternative: Alternative = "two-sided",
    axis: Literal[0, 1, 2, -1, -2, -3] = 0,
) -> MonteCarloTestResult[onp.Array2D[np.float64]]: ...
@overload
def monte_carlo_test(
    data: onp.ToFloatND,
    rvs: _RVSCallable,
    statistic: _Statistic,
    *,
    vectorized: bool | None = None,
    n_resamples: int = 9_999,
    batch: int | None = None,
    alternative: Alternative = "two-sided",
    axis: int = 0,
) -> MonteCarloTestResult: ...
