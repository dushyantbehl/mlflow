"""
Set of SQLAlchemy database schemas supported in MLflow for tracking server backends.
"""

POSTGRES = "postgresql"
MYSQL = "mysql"
SQLITE = "sqlite"
MSSQL = "mssql"
IBM_DB2 = "ibm_db_sa"

DATABASE_ENGINES = [POSTGRES, MYSQL, SQLITE, MSSQL, IBM_DB2]
