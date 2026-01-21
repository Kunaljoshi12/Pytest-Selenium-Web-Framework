import mysql.connector


def fetch_test_cases():
    try:
        conn = mysql.connector.connect(
            host="localhost", user="root",
            password="Pass@1234kj", database="Cal"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT n1, n2 FROM calculator_databse")
        data = cursor.fetchall()

        # CONVERT DATA HERE: Convert Decimal objects to standard Floats
        processed_data = [(float(row[0]), float(row[1])) for row in data]

        cursor.close()
        conn.close()
        return processed_data  # Return the cleaned list
    except Exception as e:
        print(f"DB Error: {e}")
        return []