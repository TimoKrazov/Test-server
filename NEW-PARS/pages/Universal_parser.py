import streamlit as st
import pandas as pd
from back import backend
st.set_page_config(
    page_title="Универсальный парсер",
    page_icon= "🍔", layout="wide"
)

st.markdown("""
            <style>
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
                .new_text{
                    font-size: 20px;
                }
                ul {
                    font-size: 20px;
                }
                [data-testid="stWidgetLabel"] p {
                    color: rgb(49,51,63);
                    font-weight: 700;
                }
                p, ol, ul, dl {
                    font-weight: 700 !important;
                }
            </style>
        """, unsafe_allow_html=True)
st.markdown("""
            <style>
                /*Текст загрузки файлов*/
                [data-testid="stWidgetLabel"] {
                    color: rgb(49, 51, 63);
                }
                /*Полоса загрузки файлов*/
                [data-testid="stFileUploaderDropzone"] {
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
                [data-testid="baseButton-secondary"]{
                    background-color: rgb(153, 153, 153);
                    border: 5px solid rgb(0,80,78);
                    color: rgb(0,80,78);
                    font-weight: 700;
                }
                [data-testid="baseButton-secondary"]:active{
                    background-color: rgb(0,80,78);
                    border-color: rgb(128,128,128);
                    color: rgb(240,73,35);
                }
                [data-testid="baseButton-secondary"]:hover{
                    background-color: rgb(0,80,78);
                    border-color: rgb(0,80,78);
                    color: rgb(240,73,35);
                }
                [data-testid="baseButton-secondary"]:focus {
                    background-color: rgb(0,80,78);
                    border-color: rgb(0,80,78);
                    color: rgb(240,73,35);
                }

                [data-testid="baseButton-secondary"]:focus:not(:active) {
                    background-color: rgb(0,80,78);
                    border-color: rgb(0,80,78);
                    color: rgb(240,73,35);
                }
                        /*фон методов*/
                [data-testid="stNumberInput-Input"]{
                    background-color: rgb(153, 153, 153);
                    color: rgb(0,80,78);
                }
                [data-testid="stNumberInputContainer"]{
                    border-bottom-color:rgb(153, 153, 153);
                    border-top-color: rgb(153, 153, 153);
                    border-right-color: rgb(153, 153, 153);
                    border-left-color: rgb(153, 153, 153);
                    background: rgb(153, 153, 153);
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
                }
                [data-testid="stNumberInput-StepDown"]{
                    border: 2px solid rgb(240, 73, 35);
                    border-radius: 5px;
                    color: rgb(240, 73, 35);
                    background: rgb(0,80,78);
                }
                [data-testid="stNumberInput-StepUp"]{
                    border: 2px solid rgb(240, 73, 35);
                    border-radius: 5px;
                    color: rgb(240, 73, 35);
                    background: rgb(0,80,78);
                    margin-left: 3px;
                }
                [data-testid="stNumberInput-StepDown"]:hover:enabled, [data-testid="stNumberInput-StepDown"]:focus:enabled,[data-testid="stNumberInput-StepUp"]:hover:enabled, [data-testid="stNumberInput-StepUp"]:focus:enabled {
                    background: rgb(0,80,78);
                }
                [data-testid="stFileUploaderFileName"] {
                    color: rgb(49, 51, 63);
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
            
            if st.session_state["selected_ranges"] != []:
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
                key = st.button("Очистить все диапазоны")
                if key:
                    st.session_state["selected_ranges"] = []
                if st.session_state["selected_ranges"] != []:
                    if selected_ranges:
                        st.write("Выбранные диапазоны:")
                        for i in range(1, len(selected_ranges) + 1):
                            st.write(f"Диапазон {i}:")
                            st.write(backend.chooses_ranges(df, selected_ranges[i - 1]))
             # Удаляет со 2 нажатия, Егор исправь
            
            # with st.sidebar:
            #     option = st.selectbox(
            #         '',
            #         ("Удаление диапазона строк по условию", "Удаление диапазонов столбцов по условию",
            #          "Смещение некой области"),
            #         index=None,
            #         placeholder="Выберите метод..."
            #     )
            #     col3, col4 = st.columns(2)
            #     if option == "Удаление диапазона строк по условию":
            #         comand = 'delete_srt'
            #         max_row_value = len(df)
            #         with col3:
            #             start_row = st.number_input("Начальная строка", min_value=0, max_value=max_row_value, value=0,
            #                                         key="start_row")
            #         with col4:
            #             end_row = st.number_input("Конечная строка", min_value=start_row, max_value=max_row_value,
            #                                       value=max_row_value, key="end_row")
            #         st.write("P.S. Если Строка одна и та же, то вставляется одно и то же значение в оба поля")
            #     elif option == "Удаление диапазонов столбцов по условию":
            #         comand = 'delete_stolb'
            #         max_col_value = len(df.columns)
            #         with col3:
            #             start_col = st.number_input("Начальный столбец", min_value=0, max_value=max_col_value, value=0,
            #                                         key="start_col")
            #         with col4:
            #             end_col = st.number_input("Конечный столбец", min_value=start_col, max_value=max_col_value,
            #                                       value=max_col_value, key="end_col")
            #         st.write("P.S. Если столбец один и тот же, то вставляется одно и то же значение в оба поля")
