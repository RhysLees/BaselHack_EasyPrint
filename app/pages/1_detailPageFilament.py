import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page

###### Button ######
if st.button("Go Back", key="go_back_button"):
    #del st.session_state.selected_filament
    switch_page("easyprintfrontpage")

# Add custom CSS to style and position the button
st.markdown(
    f"""
    <style>
    #go_back_button {{
        position: absolute;
        top: 10px;
        right: 10px;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)
###### Button ######


#-----------Fetching Data----#
# st.title(st.session_state.selected_filament)

# Add space between rows
st.markdown('## Filament Details')

image = st.image("pages/filament.png", caption="PLA Filament")

# Create a CSS class for the separator line
st.write(
    f"""<style>
    .separator {{
        margin: 1rem 0;
        border-top: 1px solid #ccc;
    }}
    </style><div class="separator"></div>""",
    unsafe_allow_html=True,
)


df_filaments = pd.DataFrame(st.session_state.selected_filament)
print(type(df_filaments))

col1, col2, col3 = st.columns(3)
col1.metric("Manufacturer", df_filaments['Filament'].values[0])
col2.metric("Product Line", df_filaments['Productionline'].values[0])
col3.metric("Material", df_filaments['Material'].values[0])

# Add a separator line after Row A
st.write(
    f"""<style>
    .separator {{
        margin: 1rem 0;
        border-top: 1px solid #ccc;
    }}
    </style><div class="separator"></div>""",
    unsafe_allow_html=True,
)

# Row A
left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.write("Diameter")
    st.text(df_filaments['Diameter'].values[0])
with middle_column:
    st.write("Color")
    st.text(df_filaments['Color'].values[0])
with right_column:
    st.write("Properties")
    st.text(df_filaments['Prop'].values[0])

# Add a separator line after Row A
st.write(
    f"""<style>
    .separator {{
        margin: 1rem 0;
        border-top: 1px solid #ccc;
    }}
    </style><div class="separator"></div>""",
    unsafe_allow_html=True,
)

# Row B
left_column, middle_column, right_column, over_right= st.columns(4)
with left_column:
    st.write("Net Weight")
    st.text(df_filaments['NetWeig (g)'].values[0])
with middle_column:
    st.write("Price Range")
    st.text(df_filaments['PricRang (€)'].values[0])
with right_column:
    st.write("User Review")
    st.text(df_filaments['UserRev'].values[0])
with over_right:
    st.write("Hygroscopic")
    st.text(df_filaments['Hygros'].values[0])


###### Button ######
if st.button("Download", key="download1"):
    #del st.session_state.selected_filament
    switch_page("")

# Add custom CSS to style and position the button
st.markdown(
    f"""
    <style>
    #download1 {{
        position: absolute;
        top: 10px;
        right: 10px;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)
###### Button ######