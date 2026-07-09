import streamlit as st
import os

st.set_page_config(page_title="Sraghna Media", page_icon="🔴", layout="wide")

st.markdown("""
<style>
.stApp { background-color: #1a0000; }
h1, h2, h3 { color: #ff0000; }
.stButton>button { background-color: #ff0000; color: white; border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

st.title("🔴 Sraghna Media")
st.subheader("Services Divers - Infographie - Construction - Immobilier - Tracteur Agricole")

tab1, tab2, tab3 = st.tabs(["📢 الخدمات", "🖼️ المعرض", "📞 اتصل بنا"])

with tab1:
    st.markdown("### شنو كنقدمو")
    st.write("1. **Infographie** : تصاميم، لوجو، بوستات")
    st.write("2. **Construction** : بناء، ترميم، ديكور")
    st.write("3. **Immobilier** : بيع و شراء العقار")
    st.write("4. **Tracteur Agricole** : بيع و كراء")

with tab2:
    st.markdown("### معرض الأعمال")
    images = [f for f in os.listdir('.') if f.endswith(('.jpg', '.png', '.jpeg'))]
    cols = st.columns(3)
    for i, img in enumerate(images[:9]):
        cols[i%3].image(img, use_column_width=True)

with tab3:
    st.markdown("### تواصل معنا")
    st.write("📱 WhatsApp: 06XX XX")
    st.write("📍 مراكش - السراغنة")
