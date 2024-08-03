# Setting the xReverse property in Altair
import altair as alt

# ... (other chart configurations)
alt.Chart(data).mark_point().encode(
    x=alt.X('x', scale=alt.ScaleConfig(xReverse=True)),
    y='y'
)
