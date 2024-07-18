from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

# Code for connecting to database is taken from: https://www.devart.com/dbforge/mysql/studio/amazon-rds.html
DB_HOST = "mydb-instance-1.chuu4qs8k86y.us-east-1.rds.amazonaws.com"
DB_USER = "manar"
DB_PASSWORD = "B00878259"
DB_NAME = "assignment2"

def get_db_connection():
    return pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME, port=3306)


@app.route('/store-products', methods=['POST'])
def store_products():

    data = request.get_json()
    if not data or 'products' not in data:
        return jsonify({'error': 'Missing products data'}), 400

    connection = get_db_connection()
    cursor = connection.cursor()

    # Code for inserting into rds taken from https://www.devart.com/dbforge/mysql/studio/amazon-rds.html

    try:
        for product in data['products']:
            cursor.execute('INSERT INTO products (name, price, availability) VALUES (%s, %s, %s)',
                           (product['name'], product['price'], product['availability']))
        connection.commit()
        return jsonify({'message': 'Success.'}), 200
    except Exception as e:
        connection.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        connection.close()

@app.route('/list-products', methods=['GET'])
def list_products():

    connection = get_db_connection()
    cursor = connection.cursor()

    # Code for reading from into taken from https://www.devart.com/dbforge/mysql/studio/amazon-rds.html
    try:
        cursor.execute('SELECT name, price, availability FROM products')
        products = [{'name': row[0], 'price': row[1], 'availability': row[2]} for row in cursor.fetchall()]
        return jsonify({'products': products}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        connection.close()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

