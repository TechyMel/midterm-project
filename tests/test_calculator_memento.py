import datetime
from decimal import Decimal

from app.calculation import Calculation
from app.calculator_memento import CalculatorMemento


def test_memento_to_dict():
    calc = Calculation(
        operation="Addition",
        operand1=Decimal("2"),
        operand2=Decimal("3")
    )

    memento = CalculatorMemento(history=[calc])

    data = memento.to_dict()

    assert "history" in data
    assert "timestamp" in data
    assert data["history"][0]["operation"] == "Addition"
    assert data["history"][0]["result"] == "5"


def test_memento_from_dict():
    calc = Calculation(
        operation="Addition",
        operand1=Decimal("2"),
        operand2=Decimal("3")
    )

    memento = CalculatorMemento(history=[calc])

    restored = CalculatorMemento.from_dict(memento.to_dict())

    assert len(restored.history) == 1
    assert restored.history[0].operation == "Addition"
    assert restored.history[0].operand1 == Decimal("2")
    assert restored.history[0].operand2 == Decimal("3")
    assert restored.history[0].result == Decimal("5")