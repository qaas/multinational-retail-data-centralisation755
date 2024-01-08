import pandas as pd
from dateutil.parser import parse

class DataCleaning:
    
    """
    Clean a given dataframe data in-place
    TODO: Make this method accept a set of transformations on the dataframe
    rather than a hard-coded one 
    """
    def clean_user_data(self, dirty_df):
        
        dirty_df.first_name = dirty_df.first_name.astype('string')
        dirty_df.last_name = dirty_df.last_name.astype('string')

        dirty_df.date_of_birth = pd.to_datetime(dirty_df.date_of_birth, errors='coerce')

        dirty_df.company = dirty_df.company.astype('string')
        dirty_df.email_address = dirty_df.email_address.astype('string')
        dirty_df.address = dirty_df.address.astype('string')
        dirty_df.country = dirty_df.country.astype('string')
        dirty_df.country_code = dirty_df.country_code.astype('string')
        dirty_df.phone_number = dirty_df.phone_number.astype('string')

        dirty_df.join_date = pd.to_datetime(dirty_df.join_date, errors='coerce')

        dirty_df.user_uuid = dirty_df.user_uuid.astype('string')

        # remove all na rows 
        dirty_df.dropna(inplace=True)

        return dirty_df
