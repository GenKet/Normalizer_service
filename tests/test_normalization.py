from app.utils import normalization

def test_normalize_field_money():
    """
    Тестирует нормализацию строкового значения денежной суммы.
    """
    value = "10000,00 рублей"
    expected = "10000.00"
    result = normalization.normalize_field("Сумма", value)
    assert result == expected

def test_normalize_field_strip_spaces():
    """
    Тестирует нормализацию строкового значения с лишними пробелами.
    """
    value = "  тест  "
    expected = "тест"
    result = normalization.normalize_field("Пример", value)
    assert result == expected

def test_normalize_document():
    """
    Тестирует рекурсивную нормализацию документа.
    """
    doc = {
        "Оплата": {"Сумма": "10000,00 рублей"},
        "Пример": "  тест  "
    }
    normalized = normalization.normalize_document(doc)
    assert normalized["Оплата"]["Сумма"] == "10000.00"
    assert normalized["Пример"] == "тест"
