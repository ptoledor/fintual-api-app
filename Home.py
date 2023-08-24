import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pandas as pd
import numpy as np
import datetime
import request_api as fin


# Configuracion inicial --------------------------------------------------
st.set_page_config(page_title='Inicio', page_icon='🔅', layout="centered", initial_sidebar_state='expanded')

st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #F3F6FA;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar --------------------------------------------------

st.sidebar.image('img/main3.png')
with st.sidebar:
    st.title('Easy API Requests')
    st.markdown(
        """
        https://github.com/ptoledor/fintual-api-app
        """
    )
        

st.write("## Hola! 👋")
st.text('Esta es la cosa chora ;)')


dict_fondos = {
    'Very Conservative Streep':'15077',
    'Conservative Clooney': '188',
    'Moderate Pit': '187',
    'Risky Norris': '186'
}

get_id = st.selectbox('Elige un Fondo', ('Very Conservative Streep', 'Conservative Clooney', 'Moderate Pit', 'Risky Norris'))
get_from_date = st.date_input('Fecha inicial', datetime.date(2018,1,1))
get_to_date = st.date_input('Fecha final', datetime.datetime.now())


api_id = dict_fondos[get_id]
api_from_date = str(get_from_date)
api_to_date = str(get_to_date)

request_data = fin.ask_api_real_assets(api_id, api_from_date, api_to_date)
parsed_data = fin.parse_json(request_data.json(), attribute='net_asset_value')
parsed_data['net_asset_value'] = parsed_data['net_asset_value'].astype(np.float64)

get_roi = round(fin.calculate_roi(parsed_data) * 100, 2)

st.write(f'##### ROI = {get_roi}%')


st.line_chart(parsed_data.rename(columns={'date':'index'}).set_index('index'))
st.dataframe(data=parsed_data, use_container_width=True)


# arr = list(parsed_data['date'])
# fig, ax = plt.subplots()
# ax.plot(arr)
# st.pyplot(fig)



