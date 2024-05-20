import streamlit as st

st.set_page_config(
    page_title="Создатели",
    page_icon= "🍔", layout="wide"
)

# Общие настройки
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

#Индивидуалочка

st.markdown("""
            <style>
            /* Стилизация изображения в круг */
            .rounded-image {
                border-radius: 50%;
                width: 100px; /* Ширина изображения */
                height: 100px;
                display: block;
                margin-left: auto;
                margin-right: auto;
            }
            .creaters {
                margin-top: 10px;
                display: block;
                text-align: center;
                background-color: rgb(153, 153, 153);
                color: rgb(49, 51, 63);
                border-radius: 0.5rem;
                
            } 
            @media (min-width: 1170px) {
                .rounded-image {
                    width: 175px; /* Новая максимальная ширина изображения */
                    height: 175px;
                }
            }
            </style>
            """, unsafe_allow_html=True)
st.title('Универсальный парсер Excel-файлов')
st.title('Создатели')



col5, col6, col7, col8 = st.columns(4)
with col5:
    st.markdown('<img class="rounded-image" src=https://sun9-78.userapi.com/impg/NfxasRdc3eEVjCVcl1VTbRswjVQFpxHvkBTYJw/aeF13_VeD6U.jpg?size=998x2160&quality=96&sign=772de9a33934054d71542a2a77729360&type=album width="200">', unsafe_allow_html=True)
    st.markdown('<div class="creaters"> Смирнягин Руслан: тимлид и тестировщик, The KFC King!🍔 </div>', unsafe_allow_html=True)
with col6:
    st.markdown('<img class="rounded-image" src=https://sun9-65.userapi.com/impg/Qt7o-q-Q8StEgzrB13JoHf0EG18w7fgsTP2Gig/UMb3ivEqeLI.jpg?size=309x295&quality=96&sign=9b915d7b658c613730b18eeaa9b556fc&type=album width="200">', unsafe_allow_html=True)
    st.markdown('<div class="creaters"> Баирбиликтуев Николай: backend-разработка </div>', unsafe_allow_html=True)
with col7:
    st.markdown('<img class="rounded-image" src=https://sun9-63.userapi.com/impg/bP0q_JVaMOawdjRVOxA93ccBJd8-NHxX1mVf_Q/KuXIXeu7Vfc.jpg?size=236x253&quality=96&sign=5e5f68119fdb57a1fb696b9295b67a06&type=album width="200">', unsafe_allow_html=True)
    st.markdown('<div class="creaters"> Тютюнин Николай: backend-разработка </div>', unsafe_allow_html=True)
with col8:
    st.markdown('<img class="rounded-image" src=https://sun9-54.userapi.com/impg/HcFufjn39ge-XNZpuHGiJD-Jj4I-jyv3dy0gFw/wPImGzYLiSY.jpg?size=327x337&quality=96&sign=70da940d4e25757fda9b06b2d008011f&type=album width="200">', unsafe_allow_html=True)
    st.markdown('<div class="creaters"> Шакирянов Егор: frontend-разработка </div>', unsafe_allow_html=True)
