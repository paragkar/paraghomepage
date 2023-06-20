import streamlit as st

st.set_page_config(page_title = "Telecom Homepage", page_icon=":📡:", layout ='wide')

#-----------Supported Colors--------------------

"### Supported colors"

"""
- :blue[blue]
- :green[green]
- :red[red]
- :violet[violet]
- :orange[orange]
"""

#-----------Header Section----------------------

with st.container():

	st.title("An Integrated Application For The Telecom Industry")
	st.subheader("Hi, I am Parag Kar :🙏:")
	st.write("I wrote this app to tell the story about the telecom industry through Data Visulization[blue]")
	st.markdown("The app is structured in four dimensions - 1) :Spectrum Bands[blue]; 2) Auction Years; 3) Business Data; 4) Auction Data")
	st.write("Each of these dimensions has features, subfeatures and options, which enables the users to dig deeper into the finner details of the story")
	st.write("[Link to the App>](https://paragkar-spectrummaps.streamlit.app/)")

#----What the app does ------

with st.container():
	st.write("---")
	left_column, right_column = st.columns(2)
	with left_column:
		st.header("How is this app structured")
		st.write("The Dim 'Spectrum Bands' has '3' Features - 1)Spectrum Map; 2)Expiry Map; 3)Auction Map")
		st.write("The Feature 'Spectrum Map' has '3' SubFeatures - 1)Freq Layout; 2)Operator Holdings; 3) Operator %Share.\
					Each of these are specific for a band, selectable through a drop down menu, and can also be filtered down \
					to the level of specific or a group of operators.")
		st.write("Similarly the Feature 'Expiry Map' has '2' SubFeatures - 1)Freq Layout; 2)Yearly Trends;\
					Also, each of these are specific for a band, selectable through a drop down menu, and can also be filtered down \
					to the level of specific or a group of operators.")
		st.write("The Feature 'Auction Map' has '2' SubFeatures - 1)Freq Layout; 2)Yearly Trends;\
					Also, each of these are specific for a band, selectable through a drop down menu, and can also be filtered down \
					to the level of specific or a group of operators.")
