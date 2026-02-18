import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    channel = pd.read_csv("channel_data.csv")
    videos = pd.read_csv("videos_data.csv")
    return channel, videos

channel_df, videos_df = load_data()


@st.cache_data
def load_data():
    return pd.read_csv("youtube_videos.csv")

videos_df = load_data()

st.set_page_config(page_title="YouTube Analytics Dashboard", layout="wide")
st.sidebar.header("Filters")

selected_year = st.sidebar.selectbox(
    "Select Year",
    options=sorted(videos_df['publish_year'].unique())
)

filtered_df = videos_df[videos_df['publish_year'] == selected_year]


st.title("YouTube Data Analytics Dashboard")
st.markdown("Interactive analysis of YouTube channel and video performance")


st.subheader("Channel Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Subscribers", channel_df['subscribers'][0])
col2.metric("Total Views", channel_df['total_views'][0])
col3.metric("Total Videos", channel_df['total_videos'][0])


st.subheader(" Top 10 Videos by Views")

top_videos = filtered_df.head(10)

fig, ax = plt.subplots()
ax.barh(top_videos['title'], top_videos['views'])
ax.invert_yaxis()
ax.set_xlabel("Views")

st.pyplot(fig)


st.subheader(" Engagement Comparison")

fig, ax = plt.subplots()
ax.scatter(videos_df['likes'], videos_df['comments'])
ax.set_xlabel("Likes")
ax.set_ylabel("Comments")

st.pyplot(fig)


st.subheader(" Views Over Time")

videos_by_year = videos_df.groupby('publish_year')['views'].sum()

fig, ax = plt.subplots()
ax.plot(videos_by_year.index, videos_by_year.values, marker='o')
ax.set_xlabel("Year")
ax.set_ylabel("Total Views")

st.pyplot(fig)



