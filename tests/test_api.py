import pytest
from fastapi.testclient import TestClient
from main import app


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c

def test_process_json(client):
    """
    Тестирует эндпоинт /api/process для обработки JSON-запроса.
    """
    data = {
        "doc1": {
            "ДатаДокумента": "5 ноября 2022 года",
            "Продавец": [
                {"Имя": "Иванов Лев Давидович"},
                {"Имя": "Петрова Мария Васильевна"}
            ],
            "Оплата": {"Сумма": "10000,00 рублей"},
            "Покупатель": "ООО Управляющая компания «Арасака»",
            "ПредметДоговора": {
                "ВидОбъектаНедвижимости": "ЗемельныйУчасток",
                "ВидРазрешенногоИспользования": "для сельскохозяйственного производства",
                "КадастровыйНомер": "1237:09234123532:4521",
                "Площадь": "5 га"
            }
        },
        "doc2": {
            "Оплата": {
                "СрокОплаты": "в течение 30 дней со дня подписания договора"
            },
            "ПредметДоговора": {
                "Адрес": "Московская область, 5 км от ориентира Ракушки",
                "ОбъектыНаЗемельномУчастке": ["здание", "склад"],
                "ОбременениеОбъектаНедвижимости": "ипотека",
                "ОбъектПереданПокупателюДоДоговора": "НЕТ"
            }
        }
    }
    response = client.post("/api/process", json=data)
    assert response.status_code == 200
    response_json = response.json()
    assert "original" in response_json
    assert "normalized" in response_json
    assert response_json["normalized"]["doc1"]["Оплата"]["Сумма"] == "10000.00"

def test_process_xml(client):
    """
    Тестирует эндпоинт /api/process для обработки XML-запроса.
    """
    xml_data = '''
    <root>
      <doc1>
        <ДатаДокумента>5 ноября 2022 года</ДатаДокумента>
        <Продавец>
            <Имя>Иванов Лев Давидович</Имя>
        </Продавец>
        <Продавец>
            <Имя>Петрова Мария Васильевна</Имя>
        </Продавец>
        <Оплата>
            <Сумма>10000,00 рублей</Сумма>
         </Оплата>
        <Покупатель>ООО Управляющая компания «Арасака»</Покупатель>
        <ПредметДоговора>
            <ВидОбъектаНедвижимости>ЗемельныйУчасток</ВидОбъектаНедвижимости>
            <ВидРазрешенногоИспользования>для сельскохозяйственного производства</ВидРазрешенногоИспользования>
            <КадастровыйНомер>1237:09234123532:4521</КадастровыйНомер>
            <Площадь>5 га</Площадь>
        </ПредметДоговора>
      </doc1>
      <doc2>
        <Оплата>
            <СрокОплаты>в течение 30 дней со дня подписания договора</СрокОплаты>
        </Оплата>
        <ПредметДоговора>
            <Адрес>Московская область, 5 км от ориентира Ракушки</Адрес>
            <ОбъектыНаЗемельномУчастке>здание</ОбъектыНаЗемельномУчастке>
            <ОбъектыНаЗемельномУчастке>склад</ОбъектыНаЗемельномУчастке>
            <ОбременениеОбъектаНедвижимости>ипотека</ОбременениеОбъектаНедвижимости>
            <ОбъектПереданПокупателюДоДоговора>НЕТ</ОбъектПереданПокупателюДоДоговора>
        </ПредметДоговора>
      </doc2>
    </root>
    '''
    headers = {"Content-Type": "application/xml"}
    response = client.post("/api/process", data=xml_data, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert "original" in data
    assert "normalized" in data
    assert data["normalized"]["root"]["doc1"]["Оплата"]["Сумма"] == "10000.00"
