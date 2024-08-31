def get_all_the_courss():
    connection = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    if connection.is_connected():
        cursor = connection.cursor(dictionary=True)

        query = """
        INSERT INTO courses (name, start_date, end_date, cut1_percentage, cut2_percentage, cut3_percentage)
        VALUES (%s, %s, %s, %s, %s, %s)
        """


        cursor.execute(query, values)
        connection.commit()

        cursor.close()