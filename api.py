import streamlit as st
import requests

st.set_page_config(page_title="Currency Converter", page_icon="💱")
st.title("💱 Currency Converter")
st.markdown("""
<div style="
padding:20px;
border-radius:10px;
background:linear-gradient(90deg,#1e3c72,#2a5298);
text-align:center;
color:white;
">
<h2>💱 Real-Time Currency Converter</h2>
<p>Convert currencies instantly using live exchange rates.</p>
</div>
""", unsafe_allow_html=True)
st.markdown("-----")


currencies = [
    "USD",  # US Dollar
    "INR",  # Indian Rupee
    "EUR",  # Euro
    "GBP",  # British Pound
    "JPY",  # Japanese Yen
    "AUD",  # Australian Dollar
    "CAD",  # Canadian Dollar
    "CHF",  # Swiss Franc
    "CNY",  # Chinese Yuan
    "SGD",  # Singapore Dollar
    "AED",  # UAE Dirham
    "SAR",  # Saudi Riyal
    "QAR",  # Qatari Riyal
    "KWD",  # Kuwaiti Dinar
    "BHD",  # Bahraini Dinar
    "OMR",  # Omani Rial
    "PKR",  # Pakistani Rupee
    "BDT",  # Bangladeshi Taka
    "NPR",  # Nepalese Rupee
    "LKR",  # Sri Lankan Rupee
    "THB",  # Thai Baht
    "MYR",  # Malaysian Ringgit
    "IDR",  # Indonesian Rupiah
    "KRW",  # South Korean Won
    "ZAR",  # South African Rand
    "RUB",  # Russian Ruble
    "TRY",  # Turkish Lira
    "MXN",  # Mexican Peso
    "BRL",  # Brazilian Real
    "NZD"   # New Zealand Dollar
]
col1,col2 = st.columns(2)
with col1:
    source_currency = st.selectbox("From",currencies,index=1)
with col2:
    target_currency = st.selectbox("To",currencies,index=0)
url=(f"https://v6.exchangerate-api.com/v6/ea74f9a0815a64d670fc5530/latest/{source_currency}")
response=requests.get(url)
sucess=response.status_code
data=response.json()
amount = st.number_input("Enter Your Amount",value=100.0,min_value=0.0)

st.sidebar.header("ℹ️ About Project")
st.sidebar.info("""
💱 Real-Time Currency Converter

Built Using:
                
• Python              
• Streamlit
• ExchangeRate API

Supports 30+ currencies.
""")

if st.button("Convert"):
    if response.status_code == 200:
        if target_currency in data["conversion_rates"]:
            rate = data["conversion_rates"][target_currency]
            converted_amount = amount * rate
            st.success(f"{amount} {source_currency} = "f"{converted_amount:.2f} {target_currency}")
            st.metric("Exchange Rate",f"1 {source_currency} = {rate:.4f} {target_currency}")

        else:
            st.error("Invalid Target Currency")
    else:
        st.error("API Not Work Properly!!")

from datetime import datetime

st.sidebar.metric("🕒 Current Time",datetime.now().strftime("%H:%M:%S"))
st.markdown("---")
st.markdown("<center>Built with ❤️ by Sam | Powered by ExchangeRate API</center>",unsafe_allow_html=True)
