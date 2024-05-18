import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="Универсальный парсер",
    page_icon= "🏳️‍🌈", layout="wide"
)

st.markdown("""
            <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
            <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
            <span class="material-symbols-outlined">
                transgender
            </span>
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
                [data-testid="stNumberInputContainer"]{
                    border-bottom-color:rgb(255, 73, 35);
                    border-top-color: rgb(255, 73, 35);
                    border-right-color: rgb(255, 73, 35);
                    border-left-color: rgb(255, 73, 35);
                    background: rgb(255, 73, 35);
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
                /*текст ограничений*/
                .e1nzilvr5 {
                    color: rgb(240,73,35);
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
                }
            </style>
            """, unsafe_allow_html=True)

st.title('Универсальный парсер Excel-файлов')




#Некая типо логика

uploaded_files = st.file_uploader("Загрузите файлы Excel", type=["xls", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        st.write(f"###  Рассматриваемый файл: {uploaded_file.name}")
        global df
        df = pd.read_excel(uploaded_file, index_col=None)
        st.session_state.clear()

        if df.empty:
            st.write("Парсить нечего")
        else:

            new_row = pd.DataFrame([pd.Series([pd.NA] * len(df.columns))], columns=df.columns)
            # Используем метод concat() для объединения новой строки с существующим DataFrame
            df = pd.concat([new_row, df]).reset_index(drop=True)
            search = r'\b 0 | [0-9]{1000}'
            number = 1
            df.index+=1
            for column in df.columns:
                word = str(column)
                if 'Unnamed:' in word :
                    df.rename(columns={word: number}, inplace=True)
                    number+=1
                else:
                    df.at[1,column] = column
                    df.rename(columns={column: number}, inplace=True)
                    number+=1
            st.write(df)
            with st.sidebar:
                option = st.selectbox(
                    '',
                    ("Удаление диапазона строк по условию", "Удаление диапазонов столбцов по условию", "Смещение некой области"),
                    index=None,
                    placeholder="Выберите метод..."
                )
                col3, col4 = st.columns(2)
                if (option == "Удаление диапазона строк по условию"):
                    comand = 'delete_srt'
                    max_row_value = len(df)
                    with col3:
                        start_row = st.number_input("Начальная строка", min_value=0, max_value=max_row_value, value=0,
                                                key="start_row")
                    with col4:
                        end_row = st.number_input("Конечная строка", min_value=start_row, max_value=max_row_value,
                                            value=max_row_value, key="end_row")
                    st.write("P.S. Если Строка одна и та же, то вставляется одно и то же значение в оба поля")
                elif (option =="Удаление диапазонов столбцов по условию"):
                    comand = 'delete_stolb'
                    max_col_value = len(df.columns)
                    with col3:
                        start_col = st.number_input("Начальный столбец", min_value=0, max_value=max_col_value, value=0,
                                                key="start_col")
                    with col4:
                        end_col = st.number_input("Конечный столбец", min_value=start_col, max_value=max_col_value,
                                            value=max_col_value, key="end_col")
                    st.write("P.S. Если столбец один и тот же, то вставляется одно и то же значение в оба поля")

