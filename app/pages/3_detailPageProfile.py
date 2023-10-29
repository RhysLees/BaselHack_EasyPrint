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



# Add space between rows
st.markdown('## Print Profile')

image = st.image("pages/combo.png", caption="3D Printer")

df_preset = pd.DataFrame(st.session_state.selected_preset)

col1, col2, col3 = st.columns(3)
col1.metric("3d Printer Manufacturer ", df_preset['Manufacturer'].values[0])
col2.metric("Model", df_preset['Model'].values[0])
col3.metric("Source", df_preset['Source'].values[0])

col4, col5, col6 = st.columns(3)
col4.metric("Filament Manufacturer ", df_preset['Filament'].values[0])
col5.metric("Filament Type", df_preset['Productionline'].values[0])
col6.metric("","")

# Add a separator line after Row 1
st.write(
    f"""<style>
    .separator {{
        margin: 1rem 0;
        border-top: 1px solid #ccc;
    }}
    </style><div class="separator"></div>""",
    unsafe_allow_html=True,
)

st.markdown('#### Temperature Settings')

# Row 1 / Temperatures
left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.write("Printing First Layer")
    st.text(df_preset['PrintTempFirstLayer (ºC)'].values[0])
with middle_column:
    st.write("Printing Other Layer")
    st.text(df_preset['PrintTempOtherLayers (ºC)'].values[0])
with right_column:
    st.write("Bed First Layer")
    st.text(df_preset['BedTempFrstLay (ºC)'].values[0])

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.write("Bed Other Layer")
    st.text(df_preset['BedTempOthLay (ºC)'].values[0])
with middle_column:
    st.write("Enclosure First Layer")
    st.text(df_preset['EnclTempFrstLay (ºC)'].values[0])
with right_column:
    st.write("Enclosure Other Layer")
    st.text(df_preset['EnclTempOthLay (ºC)'].values[0])

# Add a separator line after Row 2
st.write(
    f"""<style>
    .separator {{
        margin: 1rem 0;
        border-top: 1px solid #ccc;
    }}
    </style><div class="separator"></div>""",
    unsafe_allow_html=True,
)

# Row2 / Filament

st.markdown('#### Filament Settings')

left_column, middle_column, right_column, over_right= st.columns(4)
with left_column:
    st.write("Extrusion Multiplier")
    st.text(df_preset['ExtrMultiplier'].values[0])
with middle_column:
    st.write("Pressure Advanced Enabling")
    st.text(df_preset['PressAdvaEnab'].values[0])
with right_column:
    st.write("Pressure Advanced")
    st.text(df_preset['PressAdv'].values[0])
with over_right:
    st.write("Smooth Time")
    st.text(df_preset['SmthTime'].values[0])

# Add a separator line after Row 3
st.write(
    f"""<style>
    .separator {{
        margin: 1rem 0;
        border-top: 1px solid #ccc;
    }}
    </style><div class="separator"></div>""",
    unsafe_allow_html=True,
)

# Row 3 - Cooling

st.markdown('#### Cooling Settings')

left_column, middle_column, right_column, over_right= st.columns(4)
with left_column:
    st.write("Cooling")
    st.text(df_preset['Cooling'].values[0])
with middle_column:
    st.write("Fan Speed Minimum")
    st.text(df_preset['FanSpeedMin'].values[0])
with right_column:
    st.write("Fan Speed Maximum")
    st.text(df_preset['FanSpeedMax'].values[0])
with over_right:
    st.write("Bridges Fan Speed")
    st.text(df_preset['BridgesFanSpeed'].values[0])

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.write("Chamber Aux Fan Speed")
    st.text(df_preset['ChamberAuxFanSpd'].values[0])
with middle_column:
    st.write("Disable Fan First X Layers")
    st.text(df_preset['DisFanFirstLayers'].values[0])
with right_column:
    st.write("Full Fan Speed at X Layer")
    st.text(df_preset['FllFanSpeedAt'].values[0])



# Add a separator line after Row 4
st.write(
    f"""<style>
    .separator {{
        margin: 1rem 0;
        border-top: 1px solid #ccc;
    }}
    </style><div class="separator"></div>""",
    unsafe_allow_html=True,
)


# Row 4 Mix

st.markdown('#### Mixed Settings')

over_left, left_column, middle_column, right_column, over_right= st.columns(5)
with over_left:
    st.write("Max Volumetric Speed")
    st.text(df_preset['MaxVolSpeed (mm^3/s)'].values[0])
with left_column:
    st.write("Retraction length")
    st.text(df_preset['RetrLengt (mm)'].values[0])
with middle_column:
    st.write("Retraction Speed")
    st.text(df_preset['RetrSpd (mm/s)'].values[0])
with right_column:
    st.write("Deretraction Speed")
    st.text(df_preset['DeRetrtSpd (mm/s)'].values[0])
with over_right:
    st.write("Recommended Speed Max")
    st.text(df_preset['RecommSpsMax (mm/s)'].values[0])




# Add a separator line at the end
st.write(
    f"""<style>
    .separator {{
        margin: 1rem 0;
        border-top: 1px solid #ccc;
    }}
    </style><div class="separator"></div>""",
    unsafe_allow_html=True,
)

###### Button ######
if st.button("Download", key="download3"):
    #del st.session_state.selected_filament
    switch_page("")

# Add custom CSS to style and position the button
st.markdown(
    f"""
    <style>
    #download3 {{
        position: absolute;
        top: 10px;
        right: 10px;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)
###### Button ######