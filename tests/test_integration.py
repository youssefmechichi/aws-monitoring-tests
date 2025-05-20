import mysql.connector
import pytest

# Paramètres de connexion RDS
config = {
    "host": "test-db.clckk0q8w2jn.eu-north-1.rds.amazonaws.com",
    "user": "admin",
    "password": "181JMT2801",
    "database": "testdb",
}

def test_insert_and_select():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    
    # Créer table temporaire
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50))")
    
    # Insérer
    cursor.execute("INSERT INTO users (name) VALUES ('Alice')")
    conn.commit()
    
    # Lire
    cursor.execute("SELECT name FROM users WHERE name='Alice'")
    result = cursor.fetchone()
    
    assert result[0] == "Alice"
    
    # Cleanup
    cursor.execute("DELETE FROM users WHERE name='Alice'")
    conn.commit()
    cursor.close()
    conn.close()
