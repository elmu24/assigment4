import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# -> Importing all important libraries

# Title of the dashboard
st.markdown("<h1 style='text-align: center;'>📊 Dashboard with Streamlit</h1>", unsafe_allow_html=True) 
st.markdown("<br>", unsafe_allow_html=True)

# Upload dataset
df = pd.read_csv("Titanic Data.csv", sep=";", header=0)
#display secondary header and widget showing used dataset
st.markdown(f"### 📂 Using dataset: `{"Titanic Data.csv" }`")

#Inserting a line (HTML-element) for visual spacing
st.markdown("<br>", unsafe_allow_html=True)

# Select important columns for the analysis and keeping those specified columns
columns_to_keep = ["PassengerId", "Survived", "Pclass", "Name", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"]
df = df[columns_to_keep]

# Display the Title 
st.markdown("## 📋 Columns in Dataset")
st.write(df.columns.tolist())

st.markdown("<br>", unsafe_allow_html=True)

# Creating the Data preview 
st.markdown("## 📄 Data Preview")
# Interactive table showing the first few rows
st.dataframe(df.head())

st.markdown("<br>", unsafe_allow_html=True)

# generates summary statistics with key figures (count, mean, std, min, max and percentiles)
filtered_stats = df.describe() 
 # Adds median since its an important key figure
filtered_stats.loc["Median"] = df.median(numeric_only=True) 

st.markdown("## 📊 Statistical Summary")
# displays filtered summary
st.write(filtered_stats)

st.markdown("<br>", unsafe_allow_html=True)

#Pie chart for gender distribution on the titanic
st.markdown("## 🎭 Gender Distribution on the Titanic")

#Counting occurence of male and female
gender_counts = df["Sex"].value_counts()
# Blue = males, Orange = females
colors = ["#1E88E5", "#FF6633"] 

#Creating the pie chart
fig, ax = plt.subplots(figsize=(2, 2))

ax.pie(
    gender_counts, 
    labels=gender_counts.index, 
    autopct="%1.2f%%", 
    colors=colors, 
    startangle=90, 
    wedgeprops={"edgecolor": "none"},
    textprops={"fontsize": 8} 
)

#Rendering matplotlib figure in the streamlit dashboard
st.pyplot(fig)

st.markdown("<br>", unsafe_allow_html=True)

# Stacked Bar chart of survival rate in percent
st.markdown("## 📊 Titanic Survival Rate")

# Counts surviving and not surviving passengers
survival_counts = df["Survived"].value_counts()
# Calculating into percent
survival_percentage = (survival_counts / survival_counts.sum()) * 100

# Creates Dataframewith the two columns
stacked_data = pd.DataFrame({
    "Not Survived": [survival_percentage[0] if 0 in survival_percentage else 0],
    "Survived": [survival_percentage[1] if 1 in survival_percentage else 0]
})
 # visual change for readability
fig, ax = plt.subplots(figsize=(5, 7)) 

# Plotting stacked bar chart
stacked_data.plot(
    kind="bar",
    stacked=True,
    color=["#55EEFF", "#DD66FF"],  
    edgecolor="none",
    ax=ax
)

# Edit sizes etc..
ax.set_xlabel("", fontsize=14)
ax.set_ylabel("Percentage (%)", fontsize=10)
ax.set_title("Titanic Survival Rates", fontsize=10)
ax.set_ylim(0, 100)
ax.set_xticks([])

# Creating necessary text
for i, (not_survived, survived) in enumerate(zip(stacked_data["Not Survived"], stacked_data["Survived"])):
    ax.text(i, not_survived / 2, f"{not_survived:.1f}%", ha="center", va="center", fontsize=8, color="black")
    ax.text(i, not_survived + survived / 2, f"{survived:.1f}%", ha="center", va="center", fontsize=8, color="black")

#Creating legend
ax.legend(["Not Survived", "Survived"], title="Legend", loc="lower right")

# Rendering pie cart
st.pyplot(fig)
