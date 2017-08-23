import cauldron as cd
import pandas as pd

df = pd.DataFrame([
    {'a': 1, 'b': 1, 'c': 1},
    {'a': 2, 'b': 2, 'c': 2},
    {'a': 3, 'b': 3, 'c': 3},
    {'a': 4, 'b': 4, 'c': 4}
])

cd.display.table(df)

cd.shared.df = df
