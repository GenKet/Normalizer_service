# 📄 Normalizer Service

**Normalizer Service** — это современный REST API сервис для обработки юридических документов в форматах JSON и XML. Он выполняет нормализацию полей, объединяет данные из нескольких документов и сохраняет результат в базе данных PostgreSQL. Проект реализован на базе FastAPI, Pydantic, SQLAlchemy и полностью готов к контейнеризации с Docker.

---

## 🛠️ Функциональность

- **Нормализация полей**  
  Приведение строковых значений к единому формату: удаление лишних пробелов, преобразование денежных сумм (например, `"10000,00 рублей"` → `"10000.00"`) и многое другое.

- **Объединение данных**  
  Интеграция нескольких документов в единый JSON-объект с сохранением исходных и нормализованных данных.

- **Сохранение в базу данных**  
  Результат обработки сохраняется в PostgreSQL через SQLAlchemy с использованием dependency injection.

- **Поддержка JSON и XML**  
  Входной формат может быть как JSON, так и XML (XML сначала преобразуется в словарь), а ответ всегда возвращается в JSON.

- **Валидация данных**  
  Использование Pydantic (с `RootModel` для корневых моделей) обеспечивает корректность и прозрачность входных данных.

---

## 🚀 Технологии

- **Python 3.10+**
- **FastAPI** – для создания REST API
- **Pydantic** – для валидации и сериализации данных
- **SQLAlchemy** – для работы с базой данных PostgreSQL
- **Docker & Docker Compose** – для контейнеризации приложения
- **pytest** – для тестирования

---

## 📁 Структура проекта

## 📁 Структура проекта

```plaintext
project/
├── app/
│   ├── __init__.py
│   ├── db/                    # Работа с базой данных
│   │   ├── __init__.py
│   │   ├── db.py              # Подключение к БД и dependency get_db
│   │   └── db_models.py       # SQLAlchemy модели
│   ├── repositories/          # Уровень доступа к данным (CRUD-операции)
│   │   ├── __init__.py
│   │   └── document_repository.py
│   ├── routers/               # Маршрутизация API
│   │   ├── __init__.py
│   │   └── document_router.py
│   ├── schemas/               # Pydantic модели (DocumentInput, ProcessedDocument)
│   │   ├── __init__.py
│   │   └── document_models.py
│   ├── services/              # Бизнес-логика обработки документов
│   │   ├── __init__.py
│   │   └── document_service.py
│   └── utils/                 # Утилиты (функции нормализации, парсинга)
│       ├── __init__.py
│       ├── body_parser.py
│       ├── normalization.py
│       └── xml_parser.py
├── tests/                     # Тесты проекта (pytest)
│   ├── conftest.py            # Фикстуры для тестирования
│   ├── test_api.py            # Интеграционные тесты API
│   └── test_normalization.py  # Юнит-тесты для утилит
├── .gitignore
├── docker-compose.yml         # Запуск приложения и PostgreSQL через Docker Compose
├── Dockerfile                 # Docker-образ приложения
├── main.py                    # Точка входа приложения FastAPI
└── requirements.txt           # Зависимости проекта

## ⚙️ Установка и запуск

### 🚀 Локальный запуск
1. **Клонирование репозитория:**
```bash
git clone https://github.com/GenKet/Normalizer_service.git
cd Normalizer_service
```
2. **Создание виртуального окружения и установка зависимостей:**
```bash
python -m venv .venv
# Для Linux/macOS:
source .venv/bin/activate
# Для Windows:
.venv\Scripts\activate

pip install -r requirements.txt
```
3.**Запуск приложения:**
```bash
uvicorn app.main:app --reload
```

### 🐳 Запуск через Docker
1. **Сборка и запуск контейнеров:**
```bash
docker-compose up --build
```

2. **Проверка работы API:**
- **API доступен:** [http://localhost:8000](http://localhost:8000)
- **PostgreSQL:** работает на порту **5432**

### 🧪 Тестирование

Для запуска тестов из корневой директории выполните следующую команду:

```bash
pytest --disable-warnings -q
```

Тесты покрывают ключевые модули приложения (API и логику нормализации).

### 📦 Контейнеризация

Проект полностью готов к запуску в контейнерах. Файлы **Dockerfile** и **docker-compose.yml** настроены для:

- **Сборки Docker-образа** приложения
- **Запуска PostgreSQL** для хранения обработанных данных
