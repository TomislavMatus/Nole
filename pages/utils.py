def surface_to_pred(surface, pred_df):
    if surface == 'Hard':
        pred_df.loc[0, 'Hard'] = 1
    else:
        pred_df.loc[0, 'Hard'] = 0

    if surface == 'Clay':
        pred_df.loc[0, 'Clay'] = 1
    else:
        pred_df.loc[0, 'Clay'] = 0

    if surface == 'Carpet':
        pred_df.loc[0, 'Carpet'] = 1
    else:
        pred_df.loc[0, 'Carpet'] = 0

    if surface == 'Grass':
        pred_df.loc[0, 'Grass'] = 1
    else:
        pred_df.loc[0, 'Grass'] = 0
    return pred_df
