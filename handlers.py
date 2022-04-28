import pymysql
import logging
import json


def get_connection():
    return pymysql.connect(
        host='3.130.126.210',
        port=3309,
        user='pruebas',
        password='VGbt3Day5R',
        database='habi_db',
    )


def filter_inmuebles():
    statement = ("""
        SELECT MVP.*
            FROM (SELECT habi_db.property.*, GREAT.status_id
                FROM (SELECT habi_db.status_history.property_id,
                    habi_db.status_history.update_date,
                    habi_db.status_history.status_id
                    FROM habi_db.status_history
                    INNER JOIN (
                        SELECT property_id, MAX(update_date) AS update_date
                        FROM habi_db.status_history
                        GROUP BY property_id
                    ) AS b ON habi_db.status_history.property_id = b.property_id
                    AND habi_db.status_history.update_date = b.update_date
                ) AS GREAT
                INNER JOIN
                habi_db.property
                ON
                    habi_db.property.id=GREAT.property_id
            ) AS MVP
            WHERE
                MVP.status_id = 3
                OR MVP.status_id = 4
                OR MVP.status_id = 5
    """)
    connection = get_connection()
    inmuebles = []
    with connection.cursor() as cursor:
        cursor.execute(statement)
        inmuebles = cursor.fetchall()
    connection.close()
    return inmuebles


def check_filters(resource, filters):
    checks = []
    for key, value in filters.items():
        if str(resource.get(str(key))) == str(value):
            checks.append(True)
        else:
            checks.append(False)
    return all(checks)


def save_filters(filters):
    try:
        with open("filters.json", 'w') as f:
            json.dump(filters, f)
    except Exception:
        logging.error(
            "YOU CAN NOT SAVE PARAMETERS IN JSON FILE:"
        )
