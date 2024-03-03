import mysql.connector

def create_db(hostname:str, user:str, password:str, database:str):
    """ A function to create a database in MySQL

    Args:
        hostname (str): hostname of the MySQL server
        user (str): user name of the MySQL server
        password (str): Password of the MySQL server
        database (str): Database name to be created
        
    Returns:
        None
    """
    connection = mysql.connector.connect(
        host=hostname,
        user=user,
        password=password)
    cursor = connection.cursor()
    cursor.execute(f"CREATE DATABASE {database}")
    cursor.close()
    connection.close()
    
def execute_query(connection, query:str):
    """ A function to execute a query in MySQL

    Args:
        connection: mysql.connector.connection.MySQLConnection
        query (str): Query to be executed
        
    Returns:
        None
    """
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.close()
    
def create_connection(hostname, user, password, database):
    """ A function to create a connection to a MySQL database

    Args:
        hostname (str): hostname of the MySQL server
        user (str): user name of the MySQL server
        password (str): Password of the MySQL server
        database (str): Database name to be created

    Returns:
        connection: mysql.connector.connection.MySQLConnection
    """
    connection = mysql.connector.connect(
        host=hostname,
        user=user,
        password=password,
        database=database)
    return connection