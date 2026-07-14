import streamlit as st
from llm_summarize import generate_summary

st.set_page_config(page_title="Customer 360 AI", layout="wide")

st.title("Customer 360 Dashboard")

customers = [
    "ABC Technologies",
    "XYZ Solutions"
]

customer = st.selectbox(
    "Select Customer",
    customers
)

if st.button("Generate AI Summary"):

    with st.spinner("Analyzing Customer..."):

        result = generate_summary(customer)

    st.success("Analysis Complete")

    # -------------------------
    # Customer Health Score
    # -------------------------
    st.subheader("📊 Customer Health Score")

    health_score = 42

    if health_score >= 80:
        st.success(f"Health Score: {health_score}/100 🟢 Healthy")
    elif health_score >= 50:
        st.warning(f"Health Score: {health_score}/100 🟡 At Risk")
    else:
        st.error(f"Health Score: {health_score}/100 🔴 Critical")

    # -------------------------
    # Data Sources
    # -------------------------
    st.subheader("📂 Data Sources Used")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.success("✔ CRM")

    with col2:
        st.success("✔ Support Tickets")

    with col3:
        st.success("✔ Emails")

    col4, col5 = st.columns(2)

    with col4:
        st.success("✔ Slack")

    with col5:
        st.success("✔ Product Usage")

    # -------------------------
    # AI Summary
    # -------------------------
    st.subheader("🤖 AI Customer Summary")

    st.markdown(result)

    # -------------------------
    # Next Best Actions
    # -------------------------
    st.subheader("🎯 Next Best Actions")

    st.warning("📞 Contact customer within the next 48 hours.")

    st.warning("🛠 Escalate the Payment API Timeout issue to Engineering.")

    st.info("👨‍🏫 Schedule a personalized onboarding session.")

    st.info("💰 Discuss renewal pricing after resolving technical issues.")

    st.info("📊 Monitor customer usage until renewal.")

    # -------------------------
    # Recent Signals
    # -------------------------
    st.subheader("📌 Recent Customer Signals")

    st.write("📧 Email: Customer requested a discount.")
    st.write("🎫 Support Ticket: Payment API Timeout.")
    st.write("📉 Product Usage: Down by 35%.")
    st.write("📅 Renewal Due: 20 days remaining.")