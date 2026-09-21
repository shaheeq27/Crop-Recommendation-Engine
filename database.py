import os
import psycopg2

DB_CONFIG = {
    "dbname": os.getenv("DB_NAME", "crop_recommendation"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", ""),
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5432")
}


def get_connection():
    return psycopg2.connect(**DB_CONFIG)


def get_cached_weather(city):

    with get_connection() as conn:
        cur = conn.cursor()

        cur.execute(
            "SELECT temperature, rainfall, humidity FROM weather_cache WHERE city=%s",
            (city,)
        )

        result = cur.fetchone()

        if result:
            return {
                "temperature": result[0],
                "rainfall": result[1],
                "humidity": result[2]
            }

    return None


def store_weather(city, temp, rain, humidity):

    with get_connection() as conn:
        cur = conn.cursor()

        cur.execute(
            """
            INSERT INTO weather_cache(city, temperature, rainfall, humidity)
            VALUES(%s,%s,%s,%s)
            ON CONFLICT(city)
            DO UPDATE SET
            temperature=EXCLUDED.temperature,
            rainfall=EXCLUDED.rainfall,
            humidity=EXCLUDED.humidity
            """,
            (city, temp, rain, humidity)
        )

        conn.commit()
