import streamlit as st
import pandas as pd
import time

from core.pipeline import run

st.set_page_config(
    page_title="MCU SCADA Dashboard",
    layout="wide"
)

st.title("⚡ Distributed MCU SCADA Dashboard")

# ================= SIDEBAR =================
st.sidebar.title("⚙️ Control Panel")
speed = st.sidebar.slider("Speed", 0.05, 1.0, 0.2)

# ================= DATA =================
log = []

placeholder = st.empty()

# ================= LOOP =================
for i in range(60):

    data, metrics = run()
    v, c, p, r, status = data

    log.append({
        "voltage": v,
        "current": c,
        "power": p,
        "rms": r,
        "status": status,
        "latency": metrics.avg_latency()
    })

    df = pd.DataFrame(log)

    # ================= TOP METRICS (RAPI GRID) =================
    with placeholder.container():

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("⚡ Voltage", f"{v:.2f}")
        col2.metric("🔌 Power", f"{p:.2f}")
        col3.metric("⏱ Latency", f"{metrics.avg_latency():.4f}")
        col4.metric("📡 Status", status)

        st.divider()

        # ================= TABS (INI KUNCI BIAR GA PANJANG) =================
        tab1, tab2, tab3 = st.tabs([
            "📊 Monitoring",
            "📈 Analytics",
            "📁 System Log"
        ])

        # ===== TAB 1: MONITORING =====
        with tab1:
            c1, c2 = st.columns(2)

            with c1:
                st.subheader("Power Trend")
                st.line_chart(df["power"])

            with c2:
                st.subheader("Voltage Trend")
                st.line_chart(df["voltage"])

        # ===== TAB 2: ANALYTICS =====
        with tab2:
            c1, c2 = st.columns(2)

            with c1:
                st.subheader("Latency Trend")
                st.line_chart(df["latency"])

            with c2:
                st.subheader("Status Distribution")
                st.bar_chart(df["status"].value_counts())

        # ===== TAB 3: LOG =====
        with tab3:
            st.subheader("Live System Log")

            # tampilkan hanya 10 data terakhir (biar ga scroll panjang)
            st.dataframe(df.tail(10), use_container_width=True)

        # ================= EXPANDER (optional detail) =================
        with st.expander("🔍 Debug Info (Node-Level)"):
            st.json({
                "voltage": v,
                "current": c,
                "power": p,
                "rms": r,
                "status": status
            })

    time.sleep(speed)