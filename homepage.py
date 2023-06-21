from PIL import Image

import streamlit as st

import requests

from streamlit_lottie import st_lottie

st.set_page_config(page_title = "Telecom Homepage", page_icon=":📡:", layout ='wide')

#--------hide streamlit style and buttons--------------

hide_st_style = '''
				<style>
				#MainMenu {visibility : hidden;}
				footer {visibility : hidder;}
				header {visibility :hidden;}
				<style>
				'''
st.markdown(hide_st_style, unsafe_allow_html =True)


#--------Functions for loading File Starts---------------------

def load_lottieurl(url):
	r = requests.get(url)
	if r.status_code !=200:
		return None
	return r.json()


#Use local CSS

def local_css(file_name):
	with open(file_name) as f:
		st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

local_css("style/style.css")


#-----------Load Assets-------------------------

lottie_ani1 = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_cuKhxGQKFB.json")
lottie_ani2 = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_cVcpBM.json")
parag_photo = Image.open("parag_kar.jpg")
video_file = open("telecomapp.mp4", "rb")
video_file2 = open("telecomapp2.mp4", "rb")
video_file3 = open("telecomapp3.mp4", "rb")
video_bytes = video_file.read()
video_bytes2 = video_file2.read()
video_bytes3 = video_file3.read()


#-----------Header Section----------------------

with st.container():

	title_column, image_column = st.columns((4,1))

	with title_column:

		st.title("An Integrated Application For The Telecom Industry")
		st.subheader("Hi, I am Parag Kar :🙏:")
		st.write("I wrote this app to tell the story about the telecom industry through :blue[Visulization] of Data")
		st.write("The Idea is to make these :blue[Visulizations] Simple and Uniform Across the whole App")
		st.write("The app is structured in four dimensions - 1) :green[Spectrum Bands]; 2) :red[Auction Years]; 3) :violet[Business Data]; 4) :orange[Auction Data]")
		st.write("Each of these dimensions has features, subfeatures and options, which enables the users to dig deeper into the finner details of the story")
		st.write("[Link to the App>](https://paragkar-spectrummaps.streamlit.app/)")
		st.write("username - guest; password - abc123")
	with image_column:
		st.image(parag_photo)

#----What the app does ------

with st.container():
	st.write("---")
	left_column, right_column = st.columns((2,1))
	with left_column:
		st.header("How is this app structured")
		st.write("The Dimension :green['Spectrum Bands'] has '3' Features - 1) Spectrum Map; 2) Expiry Map; 3) Auction Map")
		st.write("The Feature :blue['Spectrum Map'] has '3' SubFeatures - 1) Freq Layout; 2) Operator Holdings; 3) Operator %Share.\
					Each of these are specific for a band, selectable through a drop down menu, and can also be filtered down \
					to the level of specific or a group of operators.")
		st.write("Similarly the Feature :blue['Expiry Map'] has '2' SubFeatures - 1) Freq Layout; 2) Yearly Trends;\
					Also, each of these are specific for a band, selectable through a drop down menu, and can also be filtered down \
					to the level of specific or a group of operators.")
		st.write("The Feature :blue['Auction Map'] has '2' SubFeatures - 1) Freq Layout; 2) Yearly Trends;\
					Also, each of these are specific for a band, selectable through a drop down menu, and can also be filtered down \
					to the level of specific or a group of operators.")
		st.write("---")
		st.write("The Dimension :red['Auction Years'] has '2' Features - 1) Band Metric; 2) Operator Metric")
		st.write("The Feature :blue['Band Metric'] has '7' SubFeatures, each provides an integrated snapshot of all spectrum bands for the selected CY\
			      for the selected SubFeature- for eg. 'Reserve Price', 'Auction Price' etc.")
		st.write("The Feature :blue['Operator Metric'], has '2' SubFeatures - 1)Total Outflow; 2)Total Purchase")
		st.write("Both these SubFeatures can be furthered  filtered by the Bands or by the Calender Years.")
		st.write("---")
		st.write("The Dimension :violet['Business Data'] as of date has '7' Features - These relate to various dimensions of the telecom business.\
			Such as 5GBTS Trends, Subscribers Trends, Revenue Trends etc. I will keep expanding these features further on an ongoing basis \
			as and when possible.")
		st.write("---")
		st.write("Finally, the dimension :orange['Auction Data'] is the aggregation of the simulation of all spectrum auctions that\
			has taken place in the past since 2010. This has extensive features for enabling the user to view the auction from all angles\
			and conclude who has bid where and why and what were the implications on the other bidders.")
		st.write("Currently the app is free but protected by a password. I will share this with those who are interested.")
		st.write("I will be eagerly seeking valuable feedback for improving this app further, so that it can become more useful for \
			not only exploring the intricacies of the telecom industry, but learning from our past experiences.")
		st.write("I plan to load this app on the home page of my site here -> (https://paragkar.com/)")
		st.write("This site is configured to work optimally for Desktop, so for best performance limit your to this enviornment.\
			Also, though I have made all the effort to ensure the fedility of data, but chances of inaccuries cannot be ruled out\
			I plan to correct these based on your valuable feedback. Thanks in advance.")
		st.write("Finally, allow sometime for the program to boot up with all the data loaded to the memory so that the heatmap charts can get rendered easily")
	with right_column:
		st.video(video_bytes)
		st.video(video_bytes2)
		st.video(video_bytes3)

		# st_lottie(lottie_ani1, key='telecomdata1')
		# st_lottie(lottie_ani2, key='telecomdata2')

with st.container():
	st.write("---")
	st.header("Please Provide Your Valuable Feedback")
	st.write("##")

	# Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
	contact_form = """
	<form action="https://formsubmit.co/PKAR@OUTLOOK.COM" method="POST">
		<input type="hidden" name="_captcha" value="false">
		<input type="text" name="name" placeholder="Your name" required>
		<input type="email" name="email" placeholder="Your email" required>
		<textarea name="message" placeholder="Your message here" required></textarea>
		<button type="submit">Send</button>
	</form>
	"""
	left_column, right_column = st.columns(2)
	with left_column:
		st.markdown(contact_form, unsafe_allow_html=True)
	with right_column:
		st.empty()
