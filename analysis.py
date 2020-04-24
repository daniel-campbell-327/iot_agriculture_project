import pandas as pd


def get_next_state(curr_state):
    analysis_data = pd.read_csv('transform.txt')
    filter_last = analysis_data['next_state'] > 0
    analysis_data = analysis_data.where(filter_last)
    adf = pd.DataFrame(analysis_data)

    adf = adf.groupby(['current_state', 'next_state'])['id'].count().\
        reset_index(name='count')

    adf['sum'] = adf['count'].groupby(adf['current_state']).transform('sum')
    adf['probability'] = adf['count']/adf['sum']
    adf = (adf.loc[adf['current_state'] == curr_state])
    del adf['count']
    del adf['sum']
    max_adf = adf.groupby(['current_state']).max()
    max_pred_value = max_adf.iloc[0]['probability']
    adf = adf.loc[adf['probability'] == max_pred_value]
    return adf.iloc[0]['next_state']

