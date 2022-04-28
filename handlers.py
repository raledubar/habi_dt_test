import pymysql


# allowed_states = ("pre_venta", "en_venta", "vendido")
allowed_states = (2, 40, 50)


def get_connection():
    return pymysql.connect(
        host='3.130.126.210',
        port=3309,
        user='pruebas',
        password='VGbt3Day5R',
        database='habi_db',
    )


def get_inmuebles():
    connection = get_connection()
    inmuebles = []
    statement = ("""
        SELECT id, address, city, price, description, year
        FROM habi_db.property
        WHERE (
            id IN (
                SELECT property_id FROM (
                    SELECT property_id, status_id FROM(
                        SELECT property_id FROM (
                            SELECT property_id, MAX(update_date) AS recent
                            FROM habi_db.status_history
                            GROUP BY property_id
                        ) AS sub
                    )
                    WHERE (
                        status_id=%d
                        OR status_id=%d
                        OR status_id=%d
                    )
                )
            )
        )
    """ % (allowed_states[0], allowed_states[1], allowed_states[2]))
    with connection.cursor() as cursor:
        cursor.execute(statement)
        inmuebles = cursor.fetchall()
    connection.close()
    return inmuebles


def filter_inmuebles():
    connection = get_connection()
    inmuebles = []
    # statement = ("""
    #      SELECT property_id FROM (
    #                  SELECT property_id, status_id, MAX(update_date) AS recent
    #                  FROM habi_db.status_history
    #                  GROUP BY property_id
    #              ) sub
    #             WHERE (
    #                     status_id=%d
    #                     OR status_id=%d
    #                     OR status_id=%d
    #             )
                
    # """ % (allowed_states[0], allowed_states[1], allowed_states[2]))
    # statement = ("""
    #     SELECT habi_db.property.*, last.dat, last.status_id
    #     FROM (
    #         SELECT property_id, status_id, MAX(update_date) AS dat
    #         FROM habi_db.status_history
    #         GROUP BY property_id, status_id
    #     ) AS last
    #   INNER JOIN
    #   habi_db.property
    #   ON
    #     habi_db.property.id=last.property_id
    # """)
    # statement = (""" 
    #     SELECT property_id, status_id, MAX(update_date) AS dat
    #     FROM habi_db.status_history
    #     GROUP BY property_id, status_id
    # """)

    statement = ("""
        SELECT habi_db.property.*, GREAT.status_id
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
    """)

    with connection.cursor() as cursor:
        cursor.execute(statement)
        inmuebles = cursor.fetchall()
    connection.close()
    return inmuebles
