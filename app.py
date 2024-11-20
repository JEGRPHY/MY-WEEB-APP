import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# App Title
st.title("🏄‍♂️ Fun with Bernoulli's Principle!")
st.subheader("Learn physics with laughter and fun!")

# Sidebar Controls
st.sidebar.title("Adjust the Simulation")
air_speed = st.sidebar.slider("Air Speed (m/s)", 1, 100, 10)
pipe_radius = st.sidebar.slider("Pipe Radius (cm)", 1, 10, 5)

# Calculation
pipe_area = np.pi * (pipe_radius / 100)**2
pressure = 101325 - 0.5 * 1.225 * air_speed**2  # Bernoulli's equation

# Funny Explanation
st.write(f"💨 When air speed is **{air_speed} m/s**, the pressure drops to **{int(pressure)} Pa**!")
st.write("The faster the air, the lower the pressure. Remember, **air molecules** are like racing chickens 🐓—the faster they run, the less they press down!")

# Visualization
x = np.linspace(0, 10, 100)
y = 1 / (x + 1)
fig, ax = plt.subplots()
ax.plot(x, y, label="Pressure vs. Speed", color="dodgerblue")
ax.set_xlabel("Speed (m/s)")
ax.set_ylabel("Pressure (Pa)")
ax.legend()
st.pyplot(fig)

# Funny Animation (Static for now)
st.image("https://media.giphy.com/media/3o7abldj0b3rxrZUxW/giphy.gif", caption="Molecules having a race!")

# Embed Educational Videos
st.markdown("### Learn More:")
st.markdown("- [Bernoulli's Principle in Action](https://www.youtube.com/watch?v=STIV3A8kExk)")
st.markdown("- [Why Planes Fly - A Funny Explanation](https://www.youtube.com/watch?v=Gg0TXNXgz-w)")
