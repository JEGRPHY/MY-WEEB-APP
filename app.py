import streamlit as st

# App Title
st.title("ئامادەیی ڕەنگینی کچان")
st.subheader("Engage, Learn, and Explore Physics")

# Sidebar Navigation
st.sidebar.title("بەشەکان")
menu = st.sidebar.radio("Go to:", ["Home", "Lessons", "Simulations", "Videos", "Gallery", "Resources"])
if menu == "Home":
    st.header("ئامادەیی ئیشقی کوڕان)
    st.write("""
    This platform is designed to help students access lessons, explore simulations, 
    watch videos, and collaborate effectively. Use the navigation bar to explore different sections.
    """)
    st.image("https://via.placeholder.com/800x300", caption="Physics in Action")

# Lessons Section
elif menu == "Lessons":
    st.header("Lessons")
    st.write("Choose a topic below to access lesson materials:")
    topics = ["Mechanics", "Thermodynamics", "Electricity & Magnetism", "Waves", "Optics"]
    topic = st.selectbox("Select a Topic", topics)

    if topic == "Mechanics":
        st.subheader("Mechanics")
        st.write("Here are the lessons for Mechanics:")
        st.download_button("Download Lesson 1 (PDF)", data="Lesson 1 content", file_name="lesson1_mechanics.pdf")
    elif topic == "Thermodynamics":
        st.subheader("Thermodynamics")
        st.write("Here are the lessons for Thermodynamics.")
        st.download_button("Download Lesson 1 (PDF)", data="Lesson 1 content", file_name="lesson1_thermodynamics.pdf")
    # Add more topics similarly

# Simulations Section
elif menu == "Simulations":
    st.header("Simulations")
    st.write("Explore interactive simulations below:")
    st.markdown("[PhET Simulations](https://phet.colorado.edu/)", unsafe_allow_html=True)
    st.markdown("Embed your custom simulation here:")

    # Example: Embedding a YouTube video as a simulation
    st.video("https://www.youtube.com/watch?v=ZihywtixUYo")

# Videos Section
elif menu == "Videos":
    st.header("Physics Videos")
    st.write("Watch video lessons and demonstrations:")
    st.video("https://www.youtube.com/watch?v=xyz-example")  # Replace with your video URL
    st.video("https://www.youtube.com/watch?v=abc-example")  # Replace with your video URL

# Gallery Section
elif menu == "Gallery":
    st.header("Gallery")
    st.write("Explore images from experiments or visual aids:")
    st.image("https://via.placeholder.com/400", caption="Experiment 1")
    st.image("https://via.placeholder.com/400", caption="Visual Aid for Waves")

# Resources Section
elif menu == "Resources":
    st.header("Additional Resources")
    st.write("Useful links and tools for learning physics:")
    st.markdown("- [Khan Academy](https://www.khanacademy.org/)")
    st.markdown("- [HyperPhysics](http://hyperphysics.phy-astr.gsu.edu/hbase/index.html)")
    st.markdown("- [PhET Interactive Simulations](https://phet.colorado.edu/)")

# Footer
st.sidebar.markdown("---")
st.sidebar.info("Created by Your Name | Physics Teacher")
