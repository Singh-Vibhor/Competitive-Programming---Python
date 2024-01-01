import pandas as pd

def saleOrder(df):
    df = df.values.tolist()
    df.sort(key = lambda x:x[1:])
    st = "-1"
    for x in df:
        if st != x[1]:
            st = x[1]
            mp = {}
        crr = x[3].split("/")   
        if x[2] == "Received":
            for y in crr:
                mp[y] = mp.get(y,0)+1
        else:
            for y in crr:
                if mp.get(y,0)==0:
                    return "Not Possible"
                mp[y] = mp.get(y,0)-1
    return "Possible"

df = pd.DataFrame({
    'col1': ['A', 'A', 'B', 'np.nan', 'D', 'C'],
    'col2': [2, 1, 2, 2, 2, 2],
    'col3': [0, 1, 9, 4, 2, 3],
    'col4': ['a', 'B', 'c', 'D', 'e', 'F']
})
saleOrder(df)