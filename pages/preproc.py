from sklearn.preprocessing import MinMaxScaler
scaler= MinMaxScaler()
#User input needs to be a dataframe
X_scaled = scaler.fit_transform(user_input)
