import streamlit as st
import math

# Function to calculate force or pressure based on Pascal's Principle
def calculate_pressure(force, area):
    return force / area

def calculate_force(pressure, area):
    return pressure * area

# Funny object examples
funny_examples = {
    "Elephant on a platform": 5000,  # kg
    "Basketball player dunking": 150,  # kg
    "Cat sitting calmly": 4,  # kg
    "Bag of feathers": 1,  # kg
}

# Streamlit app
st.title("Pascal's Principle Simulation")
st.subheader("Explore force and pressure with funny examples!")

# User inputs for parameters
col1, col2 = st.columns(2)

with col1:
    diameter1 = st.slider("Diameter of Small Piston (cm)", 1.0, 20.0, 5.0)
    force1 = st.number_input("Applied Force on Small Piston (N)", 0.0, 1000.0, 100.0)

with col2:
    diameter2 = st.slider("Diameter of Large Piston (cm)", 1.0, 50.0, 20.0)

# Calculate areas
radius1 = diameter1 / 2
radius2 = diameter2 / 2
area1 = math.pi * radius1**2
area2 = math.pi * radius2**2

# Pascal's principle calculations
pressure = calculate_pressure(force1, area1)
force2 = calculate_force(pressure, area2)

# Display results
st.markdown(f"### Results")
st.write(f"Pressure in the system: `{pressure:.2f} N/m²`")
st.write(f"Force exerted by the large piston: `{force2:.2f} N`")

# Funny examples
st.markdown("### Funny Examples")
st.write(f"If you apply `{force1:.2f} N`, here's what it equates to:")
for item, weight in funny_examples.items():
    force_equiv = weight * 9.8  # Convert kg to N (force)
    if force1 >= force_equiv:
        st.write(f"- It can lift: **{item}** (weight: ~{force_equiv:.2f} N)")
    else:
        st.write(f"- It **cannot** lift: **{item}** (weight: ~{force_equiv:.2f} N)")

# Visualization
st.markdown("### Visualize the Pistons")
st.write("Use the sliders above to adjust the sizes and see the forces!")
st.image("https://upload.wikimedia.org/wikipedia/commons/9/92/Pascal%27s_Law.png", caption="Pascal's Principle Illustration")
