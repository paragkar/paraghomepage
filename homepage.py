import streamlit as st

st.set_page_config(page_title = "Telecom Homepage", page_icon=":📡:", layout ='wide')

#-----------Header Section----------------------

with st.container():

	st.title("An Integrated Application For The Telecom Industry")
	st.subheader("Hi, I am Parag Kar :🙏:")
	st.write("I wrote this app to tell the story about the telecom industry through :blue[Visulization] of Data")
	st.write("The Idea is to make these :blue[Visulizations] Simple and Uniform Across the whole App")
	st.write("The app is structured in four dimensions - 1) :green[Spectrum Bands]; 2) :red[Auction Years]; 3) :violet[Business Data]; 4) :orange[Auction Data]")
	st.write("Each of these dimensions has features, subfeatures and options, which enables the users to dig deeper into the finner details of the story")
	st.write("[Link to the App>](https://paragkar-spectrummaps.streamlit.app/)")

#----What the app does ------

with st.container():
	st.write("---")
	left_column, right_column = st.columns(2)
	with left_column:
		st.header("How is this app structured")
		st.write("The Dimension :green['Spectrum Bands'] has '3' Features - 1)Spectrum Map; 2)Expiry Map; 3)Auction Map")
		st.write("The Feature :blue['Spectrum Map'] has '3' SubFeatures - 1)Freq Layout; 2)Operator Holdings; 3) Operator %Share.\
					Each of these are specific for a band, selectable through a drop down menu, and can also be filtered down \
					to the level of specific or a group of operators.")
		st.write("Similarly the Feature :blue['Expiry Map'] has '2' SubFeatures - 1)Freq Layout; 2)Yearly Trends;\
					Also, each of these are specific for a band, selectable through a drop down menu, and can also be filtered down \
					to the level of specific or a group of operators.")
		st.write("The Feature :blue['Auction Map'] has '2' SubFeatures - 1)Freq Layout; 2)Yearly Trends;\
					Also, each of these are specific for a band, selectable through a drop down menu, and can also be filtered down \
					to the level of specific or a group of operators.")
		st.write("---")
		st.write("The Dimension :red['Auction Years'] has '2' Features - 1)Band Metric; 2)Operator Metric")
		st.write("The Feature :blue['Band Metric'] has '7' SubFeatures, each provides an integrated snapshot of all spectrum bands for the selected CY\
			      for the selected SubFeature- for eg. 'Reserve Price', 'Auction Price' etc.")
		st.write("The Feature :blue['Operator Metric'], has '2' SubFeatures - 1)Total Outflow; 2)Total Purchase")
		st.write("Both these SubFeatures can be furthred filtered by the Bands or by the Calender Years.")
		st.write("---")
		st.write("The Dimension")

