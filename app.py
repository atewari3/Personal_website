import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import json

st.set_page_config(page_title="Adi's Webpage",page_icon=":wave:",layout="wide")


#assets
with open("main.css") as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

def lottie_load_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

resume_file = "Aditya Tewari's Resume.pdf"

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/atewari3/",
    "v": "https://github.com/atewari3",
}

lottie_coding = lottie_load_url("https://assets5.lottiefiles.com/private_files/lf30_wqypnpu5.json")
lottie_work = lottie_load_url("https://assets3.lottiefiles.com/packages/lf20_9e8yoqkm.json")
profile_photo = Image.open("profile_pic.png")
project_photo = lottie_load_url("https://assets9.lottiefiles.com/packages/lf20_gtbdf5vn.json")
school_logo = lottie_load_url("https://assets4.lottiefiles.com/packages/lf20_hp1tf5fx.json")
linkedin_logo = lottie_load_url("https://assets8.lottiefiles.com/private_files/lf30_tgzwnxcf.json")
phone_logo = lottie_load_url("https://assets5.lottiefiles.com/private_files/lf30_ad0z9wuy.json")
git_logo = lottie_load_url("https://assets10.lottiefiles.com/packages/lf20_6HFXXE.json")
logo_email = lottie_load_url("https://assets10.lottiefiles.com/packages/lf20_d3vw5gid.json")
resume_logo = lottie_load_url("https://lottie.host/a999f5db-2da5-4ce1-8d68-7df35c7df39b/NbF24GEZO0.json")
lifting_logo = lottie_load_url("https://lottie.host/6082eac7-4131-4101-8103-16bb6df08886/vyvhsbdxxz.json")

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

#Header Section
with st.container():
    left,useless,middle,right = st.columns((1,0.12,1,1))
    with left:
        st.title("Hi, I'm Aditya :wave:")
        st.write("I am a Student at UW-Madison who is passionate about using Python, R, SQL, and much more. for Data Science and Analytics")

        pre_left,left,pre_pre_middle,pre_middle,pre_pre_right,pre_right = st.columns((0.3,1,0.25,1,0.25,1))
        with pre_left:
            st_lottie(resume_logo,width=30)
        with left:
            st.write("[Resume](https://drive.google.com/file/d/1KAfmlX31EW8v7wFK7kpveLTsHDpUgIAc/view?usp=sharing)")
        with pre_pre_middle:
            st_lottie(linkedin_logo,width=20)
        with pre_middle:
            st.write("[LinkedIn](https://www.linkedin.com/in/atewari3/)")
        
        with pre_pre_right:
            st_lottie(git_logo,width=20)
        
        with pre_right:
            st.write("[GitHub](https://github.com/atewari3)")

    with middle:
        st.image(profile_photo,width=350)

    with right:
        st.title("Data Scientist based out of Madison,WI",)

        number_logo,number,email_logo,email = st.columns((0.15,0.5,0.15,0.8))
        with number_logo:
            st_lottie(phone_logo,width=30)
        with number:
            st.write("[414-949-9382](tel:414-949-9382)")
        with email_logo:
            st_lottie(logo_email,width=35)
        with email:
            st.write("[ATEWARI3@WISC.EDU](mailto:atewari3@wisc.edu)")


 #technical skills   
with st.container():
    st.write("---")
    left,right = st.columns((1,2))
    with left:
        st_lottie(project_photo,height=300,key="coding",width=400)

    with right:
        st.header("Tools, Languages and Technical Skills")
        st.write("""
                     

        - Programming Languages: Python (Numpy, Pandas, Matplotlib, BeautifulSoup), R, HTML, CSS, SQL

        - Languages: Hindi, Urdu, English
        
        - Data Science & Miscellaneous Technologies: A/B testing, Data Science/Data Engineering, Statistics, Time series, pipeline
        (cleansing, wrangling, visualization, modeling, interpretation), Experimental design, Hypothesis testing, OOP,  APIs, Excel, Git, Microsoft Word, Powerpoint, Excel, Google Suite, GCP (Google Cloud)
        """)

with st.container():
    st.write("---")
    left,right = st.columns((1,2))
    with left:
        st_lottie(school_logo,height=300,width=500)
    
    with right:
        st.subheader("Education")
        st.write("""
        - University of Wisconsin-Madison, School of Letters and Sciences 
        - Major: Data Science Minor: Computer Science    GPA: 4.0/4.0  
        - Relevant Coursework: Data Science with Python, Data Science Statistics, R Programming for Data Scientists
        """)


with st.container():
    st.write("---")
    left,right = st.columns((2,1))
    with left:
        st.subheader("Work Experience")
        st.subheader("C.M.A.R.P Labs | Data Scientist | Dec 2022- present | Madison, WI")
        st.write("- Visualized and analyzed mitochondrial ATP assay data using R. Used statistical analysis and tests and machine learning to predict mitochondrial ATP levels.")
        
        st.subheader("Eco-KGML group | Data Scientist | May 2023-present | Madison, WI")
        st.write("- Developed R and Python scripts for data cleaning and visualization as well as organized data pipelines to collect and standardize data for several great lakes in the Midwest, helping to generate insights and address reporting requirements.")
        
        st.subheader("UW- Madison Center For Limnology | IT Administrator | May 2023-present | Madison, WI")
        st.write("""
        - Utilized MYSQL to manipulate, modify, backup, and restore databases across a variety of servers.
        - Assisted with Website maintenance, development, troubleshooting, and general technical support for Macs and PCs.
    """)

        st.subheader("UW - Madison Department of CS | Peer Mentor | Summer 2023 |  Madison, WI")
        st.write("""
        - Provided over 50 students with academic assistance by offering problem-solving strategies, programming techniques, and explanations of data structures.
        - Fostered a collaborative learning environment in CS labs through peer-to-peer interactions.
    """)
        
    with right:
        st_lottie(lottie_work,height=500,width=600)

with st.container():
    st.write("---")
    left,right=st.columns((2,1))

    with left:
        st.subheader("Projects")

        st.subheader("[Titanic Machine Learning Modeling](https://github.com/atewari3/Titanic_MachineLearning)")
        st.write("""
        - Implemented a machine learning logistic model to predict if an individual survives the Titanic incident.
        - Demonstrated how to identify missing data, clean, visualize, create a train/test split, and apply an ML model.
    """)
            
        st.subheader("[Moneyball Sports analytics using R](https://github.com/atewari3/Moneyball-project)")
        st.write("""
        - The data product suggests replacements for Oakland As's key players based on the movie Moneyball. The project involves cleaning, filtering, and visualization. 
    """)
        
        st.subheader("[Economic Analysis via Pandas and Matplotlib](https://github.com/atewari3/Economic-Analyis-using-Pandas-and-Matplotlib-/blob/1b4622c32216c8d27536826b6ffb7b95144d04ee/Economics%20analysis%20with%20pandas%20.ipynb)")
        st.write("""
        - Conducted econometric analysis to view unemployment and participation rates during the COVID-19 pandemic in all 50 states using Pandas, Matplotlib, and the FRED economic API.
    """) 
    
    with right:
        st_lottie(lottie_coding,height=500,width=550)

with st.container():
    st.write("---")
    left,right = st.columns((2,1))
    with left:
        st.subheader("Extracurriculars")
        st.subheader("McBurney Disability Resource Center | Notetaker | September 2021 - present | Madison, WI")
        st.write("- The Mcburney Disability Center uses my notes to assist students who may have difficulty taking notes in class or may not be able to.")
        
        st.subheader("Badger volunteers | volunteer | January 2022 - present | Madison, WI")
        st.write("""- I work with a different volunteering project on a semester to semester basis to help either community in Madison or community partners abroad. 
                    - Currently, I volunteer with a conversational English project in India to help call tech center workers with collequialisms.""")
        
        st.subheader("Greater University Tutoring Services | Tutor | September 2022 -  September 2023 | Madison, WI")
        st.write("""
        - As a tutor for the Greater University Tutoring Services, I tutored general chemistry. 
        - In particular, I helped with exam and quiz preparation, visualizing theoretical chemistry concepts, and arithmetic calculations in chemistry
    """)

        st.subheader("Badger Powerlifting | Competitor | January 2022 - present |  Madison, WI")
        st.write("""
        - I complete, train, and volunteer with the badger powerlifting team. 
        - We hold powerlifting meets every year and try to promotes a healthy lifestyle through weight lifting and friendly competition. 
    """)
    with right:
        st_lottie(lifting_logo,height=500,width=550)


with st.container():
    st.write("---")
    st.header("Get in Touch With Me")
    st.write("##")


    contact_form = """
    <form action="https://formsubmit.co/atewari3@wisc.edu" method="POST">
    <input type="hidden" name = "_captcha" value="false">
     <input type="text" name="name"  placeholder = "Your Name Please" required>
     <input type="email" name="email" placeholder = "Your Email Please" required>
     <textarea name="message" placeholder = "Please Type Your Message Here" required></textarea>
     <button type="submit">Send</button>
     </form>
    """


    left,right = st.columns((2,1))
    with left:
        st.markdown(contact_form,unsafe_allow_html=True)
    with right:
        with open("contact_me.json","r") as r:
            contact_me = json.load(r)
        st.lottie(contact_me,height=300,width=525)