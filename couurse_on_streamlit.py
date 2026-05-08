import streamlit as st
import pandas as pd
import numpy as np

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="🚀 CodeSprint AI", layout="wide")

# ---------------- HEADER ----------------
st.title("🚀 CodeSprint AI Platform")
st.subheader("Learn • Compete • Analyze • Grow")

st.markdown("""
Welcome to **CodeSprint AI**, where learning meets real-world problem solving.  
Choose your path, join teams, and analyze real data!
""")

# ---------------- SIDEBAR ----------------
st.sidebar.title("👤 User Panel")
name = st.sidebar.text_input("Enter your name")

if name:
    st.sidebar.success(f"Welcome {name}!")

# ---------------- COURSE SELECTION ----------------
course = st.selectbox("📚 Select your course", ["Python", "Data Science", "Machine Learning"])
st.success(f"You selected {course}")

# ---------------- USER INPUTS ----------------
st.markdown("## 🎯 Skill & Preferences")

col1, col2 = st.columns(2)

with col1:
    lang = st.radio("Preferred Language", ["Python", "R", "Java"])
    proficiency = st.slider("Proficiency Level", 0, 10, 5)

with col2:
    team_size = st.number_input("Team Members", 1, 10)
    submission_date = st.date_input("Submission Date")

st.info(f"You chose {lang} with proficiency {proficiency}")

# ---------------- TEAM SELECTION ----------------
st.markdown("## 🤝 Join a Team")

col1, col2 = st.columns(2)

with col1:
    st.image("https://thumbs.dreamstime.com/b/cartoon-business-team-celebrating-success-illustration-diverse-group-members-depicted-cheering-major-goal-413089016.jpg", width=200)
    if st.button("Join Team A"):
        st.success("You joined Team A 🎉")

with col2:
    st.image("https://thumbs.dreamstime.com/b/brainstorming-business-plan-vector-illustration-brainstorming-business-plan-134698242.jpg",width=200)
    if st.button("Join Team B"):
        st.success("You joined Team B 🎉")

# ---------------- ADD SUBJECT ----------------
if st.checkbox("➕ Add Custom Subject"):
    subject = st.text_input("Enter subject")
    if subject:
        st.write(f"Added subject: {subject}")

# ---------------- GUIDELINES ----------------
with st.expander("📜 Competition Guidelines"):
    st.markdown("""
    1. Attend all sessions  
    2. Submit projects on time  
    3. Participate actively  
    4. Ask doubts  
    5. Practice regularly  
    """)

# ---------------- FILE UPLOAD ----------------
st.markdown("## 📂 Upload Your Dataset")

file = st.file_uploader("Upload CSV", type=["csv"])

if file:
    df_user = pd.read_csv(file)
    
    st.subheader("🔍 Data Preview")
    st.dataframe(df_user)

    st.subheader("📊 Data Summary")
    st.write(df_user.describe())

# ---------------- DASHBOARD ----------------
st.markdown("## 🏆 Coding Challenge Dashboard")

@st.cache_data
def load_challenge_data():
    np.random.seed(42)
    data = {
        "Participant": [f"User_{i}" for i in range(1, 10)],
        "Team": np.random.choice(["Team A", "Team B"], 9),
        "Problems_Solved": np.random.randint(1, 10, 9),
        "Accuracy (%)": np.random.randint(50, 100, 9),
        "Time_Taken (mins)": np.random.randint(30, 180, 9),
        "Score": np.random.randint(100, 1000, 9)
    }
    return pd.DataFrame(data)

df = load_challenge_data()

# ---------------- SIDEBAR FILTERS ----------------
st.sidebar.header("🏆 Challenge Filters")

team_filter = st.sidebar.multiselect(
    "Select Team",
    df["Team"].unique(),
    default=df["Team"].unique()
)

filtered_df = df[df["Team"].isin(team_filter)]

# ---------------- KPIs ----------------
st.subheader("📊 Performance Overview")

total_participants = filtered_df.shape[0]
avg_score = filtered_df["Score"].mean()
avg_accuracy = filtered_df["Accuracy (%)"].mean()

col1, col2, col3 = st.columns(3)

col1.metric("👥 Participants", total_participants)
col2.metric("🏅 Avg Score", f"{avg_score:.2f}")
col3.metric("🎯 Avg Accuracy", f"{avg_accuracy:.2f}%")

st.markdown("---")

# ---------------- CHARTS ----------------
st.subheader("📈 Score Distribution")
st.bar_chart(filtered_df["Score"])

st.subheader("⚡ Problems Solved per Participant")
st.bar_chart(filtered_df.set_index("Participant")["Problems_Solved"])

st.subheader("⏱ Time Taken Analysis")
st.line_chart(filtered_df["Time_Taken (mins)"])

# ---------------- LEADERBOARD ----------------
st.subheader("🥇 Leaderboard")

leaderboard = filtered_df.sort_values(by="Score", ascending=False).head(10)
st.dataframe(leaderboard, use_container_width=True)

# ---------------- RAW DATA ----------------
st.subheader("📋 Full Challenge Data")
st.dataframe(filtered_df, use_container_width=True)

# ---------------- FOOTER ----------------
st.markdown("---")
st.success("🔥Congratulations! You have successfully explored a complete Streamlit application!")