import pandas as pd

class KPIs:
    @staticmethod
    def load_data(file_path):
        return pd.read_csv(file_path)

    @staticmethod
    def get_booking_status_counts(df):
        return df['Booking Status'].value_counts()

    @staticmethod
    def get_total_rides(df):
        return df.shape[0]

    @staticmethod
    def get_completed_rides(df):
        status_counts = KPIs.get_booking_status_counts(df)
        return status_counts.get('Completed', 0)

    @staticmethod
    def get_cancelled_rides(df):
        status_counts = KPIs.get_booking_status_counts(df)
        return status_counts.get('Cancelled', 0) + status_counts.get('Incomplete', 0)

    @staticmethod
    def get_average_ride_distance(df):
        return df['Ride Distance'].mean()

    @staticmethod
    def get_peak_hours(df):
        if 'Date' in df.columns and 'Time' in df.columns:
            df_copy = df.copy()
            df_copy['Request Time'] = pd.to_datetime(df_copy['Date'] + ' ' + df_copy['Time'])
            return df_copy['Request Time'].dt.hour.value_counts().sort_index()
        return pd.Series()

    @staticmethod
    def get_top_locations(df, column, top_n=5):
        return df[column].value_counts().head(top_n)

    @staticmethod
    def get_payment_method_distribution(df):
        return df['Payment Method'].value_counts()

    @staticmethod
    def get_cancellation_reasons(df):
        cols = [
            'Reason for cancelling by Customer',
            'Driver Cancellation Reason',
            'Incomplete Rides Reason'
        ]
        reasons = pd.Series(dtype="int")
        for col in cols:
            if col in df.columns:
                reasons = pd.concat([reasons, df[col].value_counts()])
        return reasons.groupby(reasons.index).sum()

    @staticmethod
    def get_weekly_ride_trends(df):
        if 'Date' in df.columns and 'Time' in df.columns:
            df_copy = df.copy()
            df_copy['Request Time'] = pd.to_datetime(df_copy['Date'] + ' ' + df_copy['Time'])
            df_copy.set_index('Request Time', inplace=True)
            return df_copy.resample('W').size()
        return pd.Series()

    @staticmethod
    def get_monthly_ride_trends(df):
        if 'Date' in df.columns and 'Time' in df.columns:
            df_copy = df.copy()
            df_copy['Request Time'] = pd.to_datetime(df_copy['Date'] + ' ' + df_copy['Time'])
            df_copy.set_index('Request Time', inplace=True)
            return df_copy.resample('M').size()
        return pd.Series()
