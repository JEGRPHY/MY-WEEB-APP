import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Title
st.title("🎉 Funny Bernoulli Principle Simulation 🎉")
st.subheader("Learn fluid dynamics with a twist of fun!")

# Explanation
st.markdown(
    """
    According to the **Bernoulli Principle**, as the speed of a fluid increases, its pressure decreases. 
    Let's see it in action with our *speedy rubber duck*!
    """
)

# Interactive Inputs
pipe_diameter = st.slider("📏 Adjust the pipe diameter (cm):", 1, 20, 10)
fluid_speed = 100 / pipe_diameter  # Simplified relation for fun
st.write(f"💨 Fluid speed: {fluid_speed:.2f} m/s (inversely proportional to pipe diameter)")

# Visual Simulation
fig, ax = plt.subplots(figsize=(8, 4))
pipe_x = np.linspace(0, 10, 100)
pipe_y = 5 + np.sin(pipe_x) * (20 - pipe_diameter) / 5

# Pipe
ax.fill_between(pipe_x, pipe_y, 0, color="skyblue", alpha=0.6, label="Pipe")
ax.plot(pipe_x, pipe_y, color="blue", lw=2)

# Rubber Duck (or other character)
duck_x = np.linspace(0, 10, 10)
duck_y = 5 + np.sin(duck_x) * (20 - pipe_diameter) / 5 + 0.5
ax.scatter(duck_x, duck_y, color="yellow", s=100, label="Rubber Duck 🦆")
ax.legend()

# Styling
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis("off")
st.pyplot(fig)

# Funny Comments
if fluid_speed > 10:
    st.success("🚀 The rubber duck is zooming through the pipe!")
elif fluid_speed > 5:
    st.info("🐥 The rubber duck is having a good swim.")
else:
    st.warning("🐌 The rubber duck is barely moving... Increase the speed!")

# End Note
st.markdown(
    """
    **Fun Fact**: This principle is why airplanes fly and why your shower curtain attacks you 
    when you take a hot shower! Cool, right? 😉
    """
)
