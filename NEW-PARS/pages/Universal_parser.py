import streamlit as st
import pandas as pd
from back import backend

st.set_page_config(
    page_title="Универсальный парсер",
    page_icon="🏳️‍🌈", layout="wide"
)

st.markdown("""
            <style>
            /*Общие настройки*/
                /*Фон тела (Вне основного фона)*/
                body {
                    background-color: rgb(0,80,78);
                }
                /*Фон тела (основной фон)*/
                .main {
                    background-color: rgb(230, 230, 230);
                }
                /*Шапка*/
                .st-emotion-cache-18ni7ap{
                    background: rgb(128,128,128);
                }
                .st-emotion-cache-1avcm0n{
                    background: rgb(128,128,128);
                }
                /*Заголовок*/
                .st-emotion-cache-10trblm{
                    color: rgb(49, 51, 63);
                }
                /*Текст*/
                .new_text {
                    color: rgb(49, 51, 63);
                    font-size:20px;
                }
                .st-emotion-cache-1cypcdb{
                    background-color: rgb(0,80,78);
                    top: 0px;
                    height: 100% !important;
                }
                /*фон закрытия бок панели*/
                .stApp {
                    background-color: rgb(179, 179, 179);
                }
                /*цвет бок панели закрытия*/    
                .st-emotion-cache-rawifx  {
                    background-color: rgb(0,80,78);
                }
                /*цвет кнопки после зажатия*/
                .st-emotion-cache-1uy0bt2:active {
                    background: rgb(179, 179, 179);
                }
                .st-emotion-cache-1uy0bt2:visited{
                    background: rgb(240, 73, 35);
                }
                /*Остальные кнопки*/
                .st-emotion-cache-1m6wrpk{
                    color: rgb(240,73,35);
                }
                /*кнопочки*/
                .eczjsme6 {
                    background: rgb(0,80,78);
                }
                .st-emotion-cache-1we6k59:hover {
                    background: rgb(179,179,179);
                    color: rgb(240, 73, 35) !important;
                }
                .st-emotion-cache-1uy0bt2:hover {
                    background: rgb(240, 73, 35);
                }
                /*цвет элементов стримлита*/
                .st-emotion-cache-13k62yr {
                    color: rgb(240 73 35);
                }
                /*стрелка открытия бок панели*/
                .st-emotion-cache-1pbsqtx {
                    color: rgb(240, 73, 35);
                }
                .st-emotion-cache-a7yjq {
                    background-color: rgb(0,80,78);
                }
            </style>
        """, unsafe_allow_html=True)
st.markdown("""
            <style>
                /*Текст загрузки файлов*/
                .st-emotion-cache-sh2krr {
                    color: rgb(49, 51, 63);
                }
                /*Полоса загрузки файлов*/
                .e1b2p2ww15 {
                    background-color: rgb(153, 153, 153);
                    color: rgb(49, 51, 63);
                }
                .e1bju1570 {
                    color: rgb(49, 51, 63);
                }
                /*облачко*/
                .ex0cdmw0 {
                    color: rgb(240, 73, 35);
                }
                /*кнопочка*/
                .ef3psqc12 {
                    background-color: rgb(153, 153, 153);
                    border: 5px solid rgba(49, 51, 63, 0.2);
                    color: rgb(49, 51, 63);
                }
                .ef3psqc12:active {
                    background-color: rgb(153, 153, 153);
                    border-color: rgb(240,73,35);
                    color: rgb(240,73,35);
                }
                        /*фон методов*/
                .st-bb {
                    background-color: rgb(240, 73, 35);
                    color: rgb(250, 250, 250);
                }
                /*границы*/
                .st-cq {
                    border-bottom-color:rgb(255, 75, 75);
                    border-top-color: rgb(255, 75, 75);
                    border-right-color: rgb(255, 75, 75);
                    border-left-color: rgb(255, 75, 75);
                }
                .st-ba {
                    border-bottom-color:rgb(255, 75, 75);
                    border-top-color: rgb(255, 75, 75);
                    border-right-color: rgb(255, 75, 75);
                    border-left-color: rgb(255, 75, 75);
                }
                .st-emotion-cache-15wihvi, .st-emotion-cache-15wihvi:active, .st-emotion-cache-15wihvi:focus-visible {
                    background: rgb(240,73,35) !important;
                    color: rgb(0,80,78);
                }
                .st-emotion-cache-au5mm0 {
                    background:rgb(153, 153, 153);
                    color: rgb(0,80,78);
                }
                .st-emotion-cache-oteskg:hover:enabled, .st-emotion-cache-oteskg:focus:enabled {
                    background:rgb(153, 153, 153);
                    color: rgb(0,80,78);
                    transition: none 0s ease 0s;
                    outline: none;
                }
                /*текст ограничений*/
                .e1nzilvr5 {
                    color: rgb(240,73,35);
                }
                /*+ и -*/
                .st-emotion-cache-oteskg {
                    background: rgb(153, 153, 153);
                }
                /*текст +-*/
                .st-emotion-cache-f2zl0u{
                    color: rgb(0,80,78);
                }
                .st-emotion-cache-14zer8g{
                    color: rgb(0,80,78);
                }
            </style>
            """, unsafe_allow_html=True)

st.title('Универсальный парсер Excel-файлов')


#Некая типо логика
def get_files() -> list:
    uploaded_files = st.file_uploader("Загрузите файлы Excel", type=["xls", "xlsx"], accept_multiple_files=True)
    return uploaded_files


files = get_files()
if files:
    selected_ranges = st.session_state.get("selected_ranges", [])
    #Индексы изначально верные, но потом становятся на 1 больше, чем должны быть, надо исправить
    for uploaded_file in files:
        st.write(f"### {uploaded_file.name}")
        df = pd.read_excel(uploaded_file, index_col=None)
        new_row = pd.DataFrame([pd.Series([pd.NA] * len(df.columns))], columns=df.columns)
        # Используем метод concat() для объединения новой строки с существующим DataFrame
        df = pd.concat([new_row, df]).reset_index(drop=True)
        search = r'\b 0 | [0-9]{1000}'
        df.index += 1
        number = 1
        for column in df.columns:
            word = str(column)
            if 'Unnamed:' in word:
                df.rename(columns={word: number}, inplace=True)
                number += 1
            else:
                df.at[1, column] = column
                df.rename(columns={column: number}, inplace=True)
                number += 1
        st.write(df)

        if df.empty:
            st.write("Данные отсутствуют в этом файле.")
        else:
            backend.add_selected_range(df, selected_ranges)
            st.session_state["selected_ranges"] = selected_ranges
            if selected_ranges:
                if st.button("Получить данные для выбранных диапазонов"):
                    all_selected_ranges = backend.get_selected_ranges(df, selected_ranges)
                    if len(all_selected_ranges) == 1:
                        st.write("Выбранный диапазон:")
                    else:
                        st.write("Выбранные диапазоны:")
                    for selected_data in all_selected_ranges:
                        st.write(selected_data)
                    # Возможность скачать результат в виде csv-файла
                    sd = backend.convert_to_csv(all_selected_ranges)
                    download = st.download_button(
                        label="Download data as CSV",
                        data=sd,
                        file_name='Результат.csv',
                        mime='text/csv'
                    )
                if st.button("Очистить все диапазоны"):
                    st.session_state["selected_ranges"] = []
                st.write("Выбранные диапазоны:")
                for i in range(1, len(selected_ranges) + 1):
                    st.write(f"Диапазон {i}:")
                    st.write(backend.chooses_ranges(df, selected_ranges[i - 1]))
