import pandas as pd
import numpy as np
import pickle
import datetime as dt
from sklearn.base import TransformerMixin
pd.options.mode.chained_assignment = None


def load_instagram(pickle_name='pickled_inst', col_n=('Time', 'ID', 'Likes', 'Comments', 'Followers', 'Char_in_desrc',
                                                      'Tags', 'First_app'), load_old=True, time_round=True):
    import os.path as path
    org_time = path.getmtime('instagram.csv')

    def no_pickle(pickle_name):
        inst = pd.read_csv('instagram.csv', header=0, names=col_n, sep=',')
        IDs = inst['ID'].unique()
        first_app = [inst['First_app'].iloc[((inst.ID.values == ID_ex) & (inst.First_app.notna())).idxmax()]
                     for ID_ex in IDs]
        ID_first_app = dict(zip(IDs, first_app))
        inst['First_app'] = inst.apply(lambda x: ID_first_app[x['ID']], axis=1)
        inst['Time'] = pd.to_datetime(inst['Time'], unit='s')
        inst['First_app'] = pd.to_datetime(inst['First_app'], unit='s')
        first_app_date_time = pd.to_datetime(pd.Series(first_app), unit='s')
        if time_round:
            inst['Time'] = inst['Time'].dt.round('5T')
            inst['First_app'] = inst['First_app'].dt.round('5T')
            first_app_date_time = first_app_date_time.dt.round('5T')
        with open(pickle_name, 'wb') as save_pickle:
            pickle.dump(inst, save_pickle)
        with open('IDs', 'wb') as save_IDs:
            pickle.dump(IDs, save_IDs)
        with open('first_app', 'wb') as save_apps:
            pickle.dump(first_app_date_time, save_apps)
        return inst
    try:
        pickled_time = path.getmtime(pickle_name)
        if (pickled_time > org_time) and load_old:
            with open(pickle_name, 'rb') as tmp_pickle:
                instagram = pickle.load(tmp_pickle)
        else:
            instagram = no_pickle(pickle_name)
    except FileNotFoundError:
        instagram = no_pickle(pickle_name)
    return instagram


class rows_choose(TransformerMixin):
    def __init__(self, hours=range(1, 24), days=range(1, 8)):
        self.hours = hours
        self.hours_dt = [dt.timedelta(hours=h) for h in hours]
        self.days = days
        self.days_dt = [dt.timedelta(days=d) for d in days]

    def fit(self, inst_data, y=None):
        return self

    def transform(self, inst_data, y=None):
        IDs = inst_data['ID'].unique()
        first_app = [inst_data['First_app'].iloc[((inst_data.ID.values == ID_ex) &
                                                  (inst_data.First_app.notna())).idxmax()] for ID_ex in IDs]
        rows_lists_hours = np.array([[(inst_data['Time'] == (f_app + time_shift)) & (inst_data['ID'] == m_ID)
                                    for f_app, m_ID in zip(first_app, IDs)] for time_shift in self.hours_dt])
        rows_ind_hours = np.array([[row.argmax() if row.sum() > 0 else -1 for row in rows_lists]
                                   for rows_lists in rows_lists_hours])
        rows_lists_days = np.array([[(inst_data['Time'] == (f_app + time_shift)) & (inst_data['ID'] == m_ID)
                                    for f_app, m_ID in zip(first_app, IDs)] for time_shift in self.days_dt])
        rows_ind_days = np.array([[row.argmax() if row.sum() > 0 else -1 for row in rows_lists]
                                  for rows_lists in rows_lists_days])
        dt_for_hours = pd.concat({'%sh' % h: inst_data.loc[rows_ind_hours[h-1][rows_ind_hours[h-1] != -1]].dropna().set_index('ID')
                                 for h in self.hours}, sort=False)
        dt_for_days = pd.concat({'%sd' % h: inst_data.loc[rows_ind_days[h-1][rows_ind_days[h-1] != -1]].dropna().set_index('ID')
                                for h in self.days}, sort=False)
        return pd.concat([dt_for_hours, dt_for_days], sort=False)


class get_hours(TransformerMixin):
    def __init__(self, new_col_name='Int_hour', first_app_col='First_app'):
        self.new_col_name = new_col_name
        self.first_app_col = first_app_col

    def fit(self, inst_data, y=None):
        return self

    def transform(self, inst_data, y=None):
        X = inst_data.copy()
        X[self.new_col_name] = X[self.first_app_col].dt.round('1h').dt.hour
        return X


def create_time_intervals(dividing_points):
    intervals_list = ['%s-%s' % (lower_lim, dividing_points[ind])
                      for lower_lim, ind in zip(dividing_points, range(1, len(dividing_points)))]
    return intervals_list


class hours_interval(TransformerMixin):
    def __init__(self, dividing_points=range(0, 25, 6), new_col_name='Time_intervals', int_time_col='First_app'):
        self.dividing_points = dividing_points
        self.new_col_name = new_col_name
        self.int_time_col = int_time_col

    def fit(self, inst_data, y=None):
        return self

    def transform(self, inst_data, y=None):
        X = inst_data.copy()
        X[self.new_col_name] = inst_data[self.int_time_col]
        intervals_list = create_time_intervals(self.dividing_points)
        up_div_points = self.dividing_points[1:]
        intervals_ind = [X.loc[(X[self.int_time_col].dt.floor('1H').dt.hour >= low_lim) &
                               (X[self.int_time_col].dt.floor('1H').dt.hour <= up_lim)].index
                         for low_lim, up_lim in zip(self.dividing_points, up_div_points)]
        for interval, interval_ind in zip(intervals_list, intervals_ind):
            X[self.new_col_name].loc[interval_ind] = interval
        return X

      
class select_by_time(TransformerMixin):
    def __init__(self, time_freq='6h', time_col='Time', diff_col='Diff', ID_col='ID', com_col='Comments',
                 likes_col='Likes'):
        self.time_freq = time_freq
        self.time_col = time_col
        self.diff_col = diff_col
        self.ID_col = ID_col
        self.likes_col = likes_col
        self.com_col = com_col

    def fit(self, X, y=None):
        return X

    def transform(self, inst_data, y=None):
        time_range = pd.date_range(inst_data[self.time_col][0].floor('24H'),
                                   inst_data[self.time_col].iloc[-1].ceil('24H'),
                                   freq=self.time_freq)
        selected_time = inst_data.loc[inst_data[self.time_col].isin(time_range)]
        selected_time['Diff_comments'], selected_time['Diff_likes'] =\
            selected_time[self.likes_col], selected_time[self.com_col]
        for id in inst_data[self.ID_col].unique():
            sel_list = selected_time[self.ID_col] == id
            selected_time['Diff_comments'].loc[sel_list], selected_time['Diff_likes'].loc[sel_list] = \
                selected_time[self.com_col].loc[sel_list].diff(), selected_time[self.likes_col].loc[sel_list].diff()
        return selected_time.dropna()
