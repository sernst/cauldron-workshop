import cauldron as cd
import pandas as pd
from plotly import graph_objs as go


df: pd.DataFrame = cd.shared.df

cd.display.table(df)

cd.display.markdown(
    """
    # Data Frame Details
    
    - {{ min_value }}
    - {{ max_value }}
    """,
    min_value=df['a'].min(),
    max_value=df['a'].max()
)

cd.display.plotly(
    data=go.Scatter(
        x=df['a'],
        y=df['b']
    ),
    layout=go.Layout(
        title='This is an example'
    )
)
