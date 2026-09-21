# computer_club

Проект компьютерного клуба на PostgreSQL + SQLAlchemy ORM.

## Что изменено

- Добавлены декларативные ORM-модели в `app/models/`.
- `psycopg2` больше не используется напрямую в репозиториях.
- Подключение к БД выполняется через SQLAlchemy `Engine` и ORM `Session`.
- CRUD в `BaseRepository` реализован через SQLAlchemy ORM.
- Специализированные запросы репозиториев переведены на `select()` и relationships.
- `seed.py` также работает через ORM.

## Запуск

```bash
pip install -r requirements.txt
python seed.py
python main.py
```

Настройки PostgreSQL берутся из `.env`:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=computer_club_new
DB_USER=postgres
DB_PASSWORD=123
```

Также можно указать готовый `DATABASE_URL`.
