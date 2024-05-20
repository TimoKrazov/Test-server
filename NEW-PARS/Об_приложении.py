import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="Главная страница",
    page_icon= "☭", layout="wide"
)

st.markdown("""
            <style>
                body {
                    background-color: rgb(0,80,78);
                }
                /*Фон тела (основной фон)*/
                .main {
                    background-color: rgb(230, 230, 230);
                }
                [data-testid="stHeader"]{
                    background: rgb(128,128,128);
                }
                [data-testid="StyledLinkIconContainer"]{
                    color: rgb(49, 51, 63);
                }
                /*Текст*/
                [data-testid="stMarkdown"] {
                    color: rgb(49, 51, 63);
                    font-size:20px;
                }
                /*фон закрытия бок панели*/
                [data-testid="stApp"] {
                    background-color: rgb(230, 230, 230);
                    color: rgb(240 73 35);
                }
                [data-testid="stSidebar"] {
                    background-color: rgb(0,80,78);
                    top: 0px;
                    height: 100% !important;
                }
                /*цвет кнопки после зажатия*/
                [data-testid="stSidebarNavLink"] {
                    background: rgb(0,80,78);
                }
                [class="st-emotion-cache-1m6wrpk eczjsme5"] {
                    color: rgb(240,73,35);
                }
                [data-testid="stSidebarNavLink"].st-emotion-cache-18l0hbk:hover {
                    background: rgb(179, 179, 179);
                    color: rgb(240, 73, 35)
                }
                [data-testid="stSidebarNavLink"].st-emotion-cache-nziaof:visited{
                    background: rgb(240, 73, 35);
                }
                [data-testid="stSidebarNavLink"].st-emotion-cache-nziaof:hover{
                    background: rgb(240, 73, 35);
                }
                [class="st-emotion-cache-1m6wrpk eczjsme5"] {
                    color: rgb(240,73,35);
                }
                .eczjsme5{
                    color:rgb(255, 255, 255);
                }
                [class="st-emotion-cache-17lntkn eczjsme5"]{
                    color: rgb(240,73,35);
                }
                [class="st-emotion-cache-1m6wrpk eczjsme5"]{
                    color: rgb(240,73,35);
                }
                [data-testid="stSidebarNavLink"].st-emotion-cache-1we6k59:hover {
                    background: rgb(179, 179, 179);
                    color: rgb(240, 73, 35)
                }
                [data-testid="stSidebarNavLink"].st-emotion-cache-1uy0bt2:visited{
                    background: rgb(240, 73, 35);
                }
                /*стрелка открытия бок панели*/
                [data-testid="baseButton-headerNoPadding"] {
                    color: rgb(240, 73, 35);
                }
                [data-testid="stSidebarNavLink"].st-emotion-cache-1uy0bt2:hover{
                    background: rgb(240, 73, 35);
                }
            </style>
            """, unsafe_allow_html=True)

st.image('https://psv4.userapi.com/c909628/u305551478/docs/d32/894db955a411/qw.png?extra=NR4WaDxmPToQbiV7LRKJ0P9X_1TqmkGwE4c82nKUJVtl5aaeLNw-ZlYrm9ps1s7i0HS76m7umSXxps2czQz5oHmcY6w4AQhBuTk8ay55aMd6xtY1gZq2uckcG4jECcqoV-b90oMrc9RX20YdjkwP5knElg')

st.title('Универсальный парсер Excel-файлов')
st.title('Об приложении')


st.markdown('<div class = "new_text">Универсальный парсер - приложение, написанное на Python и способное преобразовывать Excel-файл в формат csv, вводя новые корректировки в файл или неизменяя его. </div>',  unsafe_allow_html= True)
st.markdown('<div class = "new_text">Полный функционал Парсера: </div>',  unsafe_allow_html= True)

