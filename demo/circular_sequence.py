"""Demonstração pública de faixas circulares 000–999, sem integração externa."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Iterable

SEQUENCE_LIMIT = 1000


class SequenceError(ValueError):
    """Entrada ou intervalo de sequência inválido."""


class SequenceOverlapError(SequenceError):
    """A faixa proposta cruza outra faixa já registrada."""


def normalize_sequence(value: str | int) -> str:
    """Valida uma sequência e devolve o valor com três dígitos."""
    raw = str(value).strip()
    if not re.fullmatch(r"\d{1,3}", raw):
        raise SequenceError("A sequência deve conter de um a três dígitos.")
    number = int(raw)
    if not 0 <= number < SEQUENCE_LIMIT:
        raise SequenceError("A sequência deve estar entre 000 e 999.")
    return f"{number:03d}"


@dataclass(frozen=True)
class SequenceRange:
    """Intervalo inclusivo dentro de um ciclo numerado a partir de 1."""

    start: str
    end: str
    cycle: int

    def __post_init__(self) -> None:
        object.__setattr__(self, "start", normalize_sequence(self.start))
        object.__setattr__(self, "end", normalize_sequence(self.end))
        if self.cycle < 1:
            raise SequenceError("O ciclo deve ser maior ou igual a 1.")

    @property
    def coordinates(self) -> tuple[int, int]:
        first = (self.cycle - 1) * SEQUENCE_LIMIT + int(self.start)
        last_cycle = self.cycle + int(int(self.end) < int(self.start))
        last = (last_cycle - 1) * SEQUENCE_LIMIT + int(self.end)
        return first, last


def ranges_overlap(first: SequenceRange, second: SequenceRange) -> bool:
    first_start, first_end = first.coordinates
    second_start, second_end = second.coordinates
    return max(first_start, second_start) <= min(first_end, second_end)


def ensure_no_overlap(
    proposed: SequenceRange,
    registered: Iterable[SequenceRange],
) -> None:
    for existing in registered:
        if ranges_overlap(proposed, existing):
            raise SequenceOverlapError(
                f"A faixa {proposed.start}–{proposed.end}, ciclo {proposed.cycle}, "
                f"sobrepõe {existing.start}–{existing.end}, ciclo {existing.cycle}."
            )


def main() -> None:
    ranges = [
        SequenceRange("850", "040", 1),
        SequenceRange("050", "060", 2),
    ]
    candidate = SequenceRange("900", "920", 1)
    ensure_no_overlap(candidate, ranges)
    print(f"Faixa {candidate.start}–{candidate.end}, ciclo {candidate.cycle}: válida")


if __name__ == "__main__":
    main()
