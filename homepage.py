import streamlit as st

st.set_page_config(page_title = "Telecom Homepage", page_icon=":📡:", layout ='wide')

#-----------Header Section----------------------

with st.container():

	st.title("An Integrated Application For The Telecom Industry")
	st.subheader("Hi, I am Parag Kar :🙏:")
	st.write("I wrote this app to tell the story about the telecom industry by visulalizing Data")
	st.write("The app is structured in four dimensions - 1) Spectrum Bands; 2) Auction Years; 3) Business Data; 4) Auction Data")
	st.write("Each of these dimensions has features and options, which enables the users to dig deeper into the finner details of the story")
	st.write("[Link to the App>](https://paragkar-spectrummaps.streamlit.app/)")

#----What the app does ------

with st.container():
	st.write("---")
	left_column, right_column = st.columns(2)
	with left_column:
		st.header("How this app works")
		st.write("##")
		st.write(
			"""

			""")
