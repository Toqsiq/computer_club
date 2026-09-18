from app.repositories import (
    TariffRepository,
    ServiceRepository,
)
from app.db import get_connection
from psycopg2.extras import RealDictCursor


def seed_data():
    with get_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:

            # 1. Статусы компьютеров
            cur.execute("""
                INSERT INTO computer_statuses (name, description) VALUES
                ('available', 'Свободен'),
                ('occupied', 'Занят'),
                ('maintenance', 'На обслуживании'),
                ('disabled', 'Отключён')
                ON CONFLICT (name) DO NOTHING;
            """)

            # 2. Статусы сессий
            cur.execute("""
                INSERT INTO session_statuses (name, description) VALUES
                ('booked', 'Забронирована'),
                ('active', 'Идёт'),
                ('completed', 'Завершена'),
                ('cancelled', 'Отменена')
                ON CONFLICT (name) DO NOTHING;
            """)

            # 3. Клуб
            cur.execute("""
                INSERT INTO clubs (name, address, phone) VALUES
                ('Chain of Computer Clubs - Центральный', 'ул. Примерная, 10', '+7 (999) 123-45-67')
                ON CONFLICT DO NOTHING
                RETURNING id;
            """)
            club = cur.fetchone()
            club_id = club["id"] if club else 1

            # 4. Тарифы
            cur.execute("""
                INSERT INTO tariffs (name, duration_minutes, price, description) VALUES
                ('Standard 1 час', 60, 150.00, 'Обычный тариф на 1 час'),
                ('VIP 1 час', 60, 250.00, 'VIP тариф на 1 час'),
                ('Standard 3 часа', 180, 400.00, 'Обычный тариф на 3 часа'),
                ('VIP 3 часа', 180, 650.00, 'VIP тариф на 3 часа'),
                ('Ночная смена 8 часов', 480, 900.00, 'Ночной тариф с 00:00 до 08:00')
                ON CONFLICT DO NOTHING;
            """)

            # 5. Услуги
            cur.execute("""
                INSERT INTO services (name, price, description) VALUES
                ('Кофе', 100.00, 'Кофе'),
                ('Энергетик', 120.00, 'Энергетический напиток'),
                ('Аренда наушников', 50.00, 'Наушники'),
                ('VIP кресло', 80.00, 'Улучшенное кресло'),
                ('Бутерброд', 90.00, 'Бутерброд')
                ON CONFLICT DO NOTHING;
            """)

            # 6. Зоны
            cur.execute("""
                INSERT INTO computer_zones (club_id, name, description, hourly_price) VALUES
                (%s, 'Standard', 'Обычная зона', 150.00),
                (%s, 'VIP', 'VIP зона', 250.00)
            """, (club_id, club_id))

            print("Данные успешно добавлены!")


if __name__ == "__main__":
    seed_data()