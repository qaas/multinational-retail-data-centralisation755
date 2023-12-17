import yaml
from sqlalchemy import create_engine
from sqlalchemy import inspect

class DatabaseConnector:
    
    def read_db_creds(self):
        """
        Reads the credentials stored in a yaml file and returns them as a dictionary.
        """
        with open('db_creds.yaml', 'r') as f:
            creds = yaml.safe_load(f)

        return creds

    def init_db_engine(self):
        """
        Initialize and return a SQLAlchemy engine to be used for sending
        and executing database commands. 
        """
        creds = self.read_db_creds()

        try:
            engine = create_engine(f"postgresql://{creds['RDS_USER']}:{creds['RDS_PASSWORD']}@{creds['RDS_HOST']}:5432/{creds['RDS_DATABASE']}",
                                    echo=False)

        except Exception as e:
            print(e)
            raise
        
        return engine
    
    def list_db_tables(self):
        """
        """
        engine = self.init_db_engine()

        inspector = inspect(engine)

        tables = []

        for table in inspector.get_table_names():
            tables.append(table)
        
        return tables

if __name__ == '__main__':
    pass