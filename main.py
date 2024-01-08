from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning


if __name__ == '__main__':
    
    db = DatabaseConnector()

    extractor = DataExtractor()
    df = extractor.read_rds_table(db, 'legacy_users')

    print(df.shape)
    print(df.dtypes)

    cleaner = DataCleaning()
    clean_df = cleaner.clean_user_data(df)

    print(clean_df.dtypes)
 