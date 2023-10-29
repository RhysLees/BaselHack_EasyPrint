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

#st.title(st.session_state.selected_printer)

# Add space between rows
st.markdown('## 3D Printer')

image = st.image("pages/printer.jpg", caption="3D Printer")

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
df_printers = pd.DataFrame(st.session_state.selected_printer)
print(type(df_printers))

col1, col2 = st.columns(2)
col1.metric("Manufacturer", df_printers['Manufacturer'].values[0])
col2.metric("Model", df_printers['Model'].values[0])

# Row A
left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.write("Build Size")
    st.text(str(df_printers['X_Size (mm)'].values[0])+ "x" +
            str(df_printers['Y_Size (mm)'].values[0])+ "x" +
            str(df_printers['Z_Size (mm)'].values[0]))
with middle_column:
    st.write("Price Range")
    st.text(df_printers['PriceRange (€)'].values[0])
with right_column:
    st.write("User Review")
    st.text(df_printers['UserRev'].values[0])

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
left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.write("Architecture Type")
    st.text(df_printers['Arch'].values[0])
with middle_column:
    st.write("Firmware")
    st.text(df_printers['FW'].values[0])
with right_column:
    st.write("Number of Extruders")
    st.text(df_printers['NumExtr'].values[0])

# Add a separator line after Row B
st.write(
    f"""<style>
    .separator {{
        margin: 1rem 0;
        border-top: 1px solid #ccc;
    }}
    </style><div class="separator"></div>""",
    unsafe_allow_html=True,
)

# Row C
left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.write("Auxiliar Part Cooling")
    st.text(df_printers['AuxPrtCool'].values[0])
with middle_column:
    st.write("Extruder Type")
    st.text(df_printers['ExtrudType'].values[0])
with right_column:
    st.write("Multi Color")
    st.text(df_printers['MultColor'].values[0])

# Add a separator line after Row C
st.write(
    f"""<style>
    .separator {{
        margin: 1rem 0;
        border-top: 1px solid #ccc;
    }}
    </style><div class="separator"></div>""",
    unsafe_allow_html=True,
)

# Row D
left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.write("Heat Chamber")
    st.text(df_printers['HeatCha'].values[0])
with middle_column:
    st.write("Filament Diameter")
    st.text(df_printers['FilDiam (mm)'].values[0])
with right_column:
    st.write("Auto Bed Leveling System")
    st.text(df_printers['AutBedLev'].values[0])


    ###### Button ######
if st.button("Download", key="download2"):
    #del st.session_state.selected_filament
    switch_page("")

# Add custom CSS to style and position the button
st.markdown(
    f"""
    <style>
    #download2 {{
        position: absolute;
        top: 10px;
        right: 10px;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)
###### Button ######