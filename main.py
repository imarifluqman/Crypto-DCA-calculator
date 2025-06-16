import streamlit as st

def calculate_additional_position(old_price, old_qty, new_price, target_price): try: old_value = old_price * old_qty x = (target_price * old_qty - old_value) / (new_price - target_price) return round(x, 6) except ZeroDivisionError: return None

st.title("DCA Entry Price Adjuster for SHORT Position")

st.markdown(""" This app helps you calculate how much more quantity to short at the current market price in order to move your average entry price to a desired level. """)

st.subheader("🔢 Input Current Position") old_price = st.number_input("Old Entry Price (e.g. 105000)", value=105000.0) old_qty = st.number_input("Old Position Quantity in BTC (e.g. 0.0054)", value=0.0054, format="%.6f")

st.subheader("🎯 Target and Market Info") target_price = st.number_input("Target Entry Price (e.g. 106300)", value=106300.0) new_price = st.number_input("Current Market Price (e.g. 106234.7)", value=106234.7)

if st.button("Calculate Additional Short Quantity"): additional_qty = calculate_additional_position(old_price, old_qty, new_price, target_price) if additional_qty is not None and additional_qty > 0: st.success(f"✅ You need to short {additional_qty} BTC more at ${new_price} to adjust your entry price to ${target_price}.") elif additional_qty is not None and additional_qty <= 0: st.warning("⚠️ Your target entry price is lower than your current entry. You may need to close or reduce your position instead.") else: st.error("❌ Error: Cannot divide by zero. Please check your inputs.")

st.markdown("---") st.markdown("Made with ❤️ using Streamlit")

