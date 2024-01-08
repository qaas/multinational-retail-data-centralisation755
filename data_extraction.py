import pandas as pd

from database_utils import DatabaseConnector

class DataExtractor:
    
    def read_rds_table(self, db: DatabaseConnector, table=None):
        """
        Extracts a database table to a pandas dataframe.
        Params: 
            db: an instance of DatabaseConnector class
            table: the table we want to read data from

        Returns: a pandas dataframe
        """

        engine = db.init_db_engine()

        df = pd.read_sql_table(table, engine)

        return df
    