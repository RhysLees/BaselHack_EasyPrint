import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.switch_page_button import switch_page
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode



#---------------------Read inn all files do df ----------------
file_path = "./3dpdatabase - 3dPrinters.csv"
df_printers = pd.read_csv(file_path)


file_path = "./3dpdatabase - Filament.csv"
df_filament = pd.read_csv(file_path)


file_path = "./3dpdatabase - Presets.csv"
df_preset = pd.read_csv(file_path)



#------------------- set upt page ---------------------------
st.set_page_config(layout='wide', initial_sidebar_state='expanded')
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
st.sidebar.header('3D Print Simplified')


#---------------------------------printer brand selector & model availability------------------------------------

st.sidebar.subheader('3D Printer Brand')
selection_manuf = st.sidebar.selectbox('', np.unique(np.insert(df_printers['Manufacturer'],0,"")))

if selection_manuf:
    df_printer_model = df_printers[selection_manuf == df_printers['Manufacturer']]
else:
    df_printer_model = df_printers

st.sidebar.subheader('3D Printer Model')
selection_model = st.sidebar.selectbox('', np.insert(df_printer_model['Model'],0,""))

#----------------------------Filament brand selector and type availability----------------------------

st.sidebar.subheader('Filament Brand')
selection_filament_manuf = st.sidebar.selectbox('', np.unique(np.insert(df_filament['Filament'],0,"")))

if selection_filament_manuf:
    df_filament_model = df_filament[selection_filament_manuf == df_filament['Filament']]
else:
    df_filament_model = df_filament

st.sidebar.subheader('Filament Product line')
selection_filament_model = st.sidebar.selectbox('', np.insert(df_filament_model['Productionline'],0,""))



#-------------------------End of left menu------------------------------------------

#st.sidebar.subheader('Filament')
#selection_filament = st.sidebar.selectbox('', np.unique(np.insert(df_filament['Productionline'],0,"")))
# st.sidebar.subheader('Line chart parameters')
# plot_data = st.sidebar.multiselect('Select data', ['temp_min', 'temp_max'], ['temp_min', 'temp_max'])
# plot_height = st.sidebar.slider('Specify plot height', 200, 500, 250)
st.sidebar.markdown('''
---
Created with :heart: by EasyPrint Team @ Basel Hack 2023
''')


# ------------------------------filters  printers--------------------------------

base_printer = df_printers
if selection_manuf:
    base_printer = df_printers
    base_printer = base_printer[base_printer['Manufacturer'] == selection_manuf]

if selection_model:
    base_printer = base_printer[base_printer['Model'] == selection_model]

# gives base printer as table of filteres printer 



#----------------------------Filters  filament---------------------------------------------



base_filament = df_filament
if selection_filament_manuf:
    base_filament = df_filament
    base_filament = base_filament[base_filament['Filament'] == selection_filament_manuf]

if selection_filament_model:
    base_filament = base_filament[base_filament['Productionline'] == selection_filament_model]
    
    
# base filament contains sorted filament df    
    
#----------------------Filter preset------------------------------------------   

base_preset = df_preset
if selection_manuf:
    base_preset = base_preset[base_preset['Manufacturer'] == selection_manuf]

if selection_model:
    base_preset = base_preset[base_preset['Model'] == selection_model]

if selection_filament_manuf:
    base_preset = base_preset[base_preset['Filament'] == selection_filament_manuf]

if selection_filament_model:
    base_preset = base_preset[base_preset['Productionline'] == selection_filament_model]

#Base preset contaisn filteres presets 

 
# --------------------------- Right side UI Tables and buttins
# st.title("EasyPrint - a better way to finding Presets")
sample_size = 10 # number of entries
max_table_height = 300   # height of the table
grid_height = 200
zero_height = 100



# -----------------------------------Logo

image = st.image("Logo_without_background.png")




#------------------------ Printer selection table ----------------------
#Infer basic colDefs from dataframe types
st.subheader("Results Printers")


selected_columns_printers = ["Manufacturer", "Model", "X_Size (mm)", "Y_Size (mm)","Z_Size (mm)"]
gb = GridOptionsBuilder.from_dataframe(base_printer[selected_columns_printers])
gb.configure_selection("single", use_checkbox=True)
gb.configure_pagination(paginationAutoPageSize=True)
gb.configure_grid_options(domLayout='normal')
gridOptions = gb.build()

grid_response = AgGrid(base_printer,gridOptions=gridOptions,height=min(max_table_height, len(base_printer) * 25+zero_height),width='100%',
    data_return_mode="FILTERED",update_mode="SELECTION_CHANGED",fit_columns_on_grid_load=True,)
selected_printer = grid_response['selected_rows']

if selected_printer not in st.session_state:
    st.session_state.selected_printer = selected_printer
    
if selected_printer != []:
    print(grid_response['selected_rows'])
    switch_page("detailpageprinter")

#-------------------------------- Filament seletion table --------------------------
st.subheader("Results Filament")
selected_columns_filament = ["Filament", "Productionline","Material", "Diameter"]
#sample_size = 10  # number of entries
#grid_height =300   # height of the table
gb = GridOptionsBuilder.from_dataframe(base_filament[selected_columns_filament])
gb.configure_selection("single", use_checkbox=True)
gb.configure_pagination(paginationAutoPageSize=True)
gb.configure_grid_options(domLayout='normal')
gridOptions = gb.build()

grid_response = AgGrid(base_filament,gridOptions=gridOptions,height=min(max_table_height, len(base_filament) * 25+zero_height),width='100%',
    data_return_mode="FILTERED",update_mode="SELECTION_CHANGED",fit_columns_on_grid_load=True,)
selected_filament = grid_response['selected_rows']

if selected_filament not in st.session_state:
    st.session_state.selected_filament = selected_filament
    
if selected_filament != []:
    print(grid_response['selected_rows'])
    switch_page("detailpagefilament")

#-------------------------------------------------55544 Preset selctalbe table ------------

st.subheader("Results Preset")
selected_columns_presets = ["Filament", "Productionline", "Manufacturer","Model", "Source" ]
gb = GridOptionsBuilder.from_dataframe(base_preset[selected_columns_presets])
gb.configure_selection("single", use_checkbox=True)
gb.configure_pagination(paginationAutoPageSize=True)
gb.configure_grid_options(domLayout='normal')
gridOptions = gb.build()

grid_response = AgGrid(base_preset,gridOptions=gridOptions,height=min(max_table_height, len(base_preset) * 25+zero_height),width='100%',
    data_return_mode="FILTERED",update_mode="SELECTION_CHANGED",fit_columns_on_grid_load=True,)
selected_preset = grid_response['selected_rows']

if selected_preset not in st.session_state:
    st.session_state.selected_preset = selected_preset
    
if selected_preset != []:
    print(grid_response['selected_rows'])
    switch_page("detailpageprofile")





