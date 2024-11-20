import streamlit as st
import math
import plotly.graph_objects as go
import numpy as np

# Function to calculate force or pressure based on Pascal's Principle
def calculate_pressure(force, area):
    return force / area

def calculate_force(pressure, area):
    return pressure * area

# Generate 3D Cylinder using mesh3d
def create_cylinder(x_center, y_center, z_bottom, radius, height, resolution=30, color="blue"):
    theta = np.linspace(0, 2 * np.pi, resolution)
    z = np.array([z_bottom, z_bottom + height])
    x = radius * np.outer(np.cos(theta), np.ones_like(z)) + x_center
    y = radius * np.outer(np.sin(theta), np.ones_like(z)) + y_center
    z = np.outer(np.ones_like(theta), z)
    return go.Mesh3d(
        x=x.flatten(),
        y=y.flatten(),
        z=z.flatten(),
        color=color,
        opacity=0.5,
    )

# Funny object examples
funny_examples = {
    "Elephant": 5000,  # kg
    "Person": 70,      # kg
    "Cat": 4,          # kg
    "Bag of feathers": 1,  # kg
}

# Streamlit app
st.title("Pascal's Principle with 3D Simulation")
st.subheader("Explore forces and pressures in 3D!")

# User inputs
col1, col2 = st.columns(2)

with col1:
    diameter1 = st.slider("Diameter of Small Piston (cm)", 1.0, 20.0, 5.0)
    force1 = st.number_input("Applied Force on Small Piston (N)", 0.0, 1000.0, 100.0)
    applied_objects = st.multiselect("Add objects to apply force (total):", list(funny_examples.keys()), ["Elephant"])

with col2:
    diameter2 = st.slider("Diameter of Large Piston (cm)", 1.0, 50.0, 20.0)

# Calculate areas and forces
radius1 = diameter1 / 2
radius2 = diameter2 / 2
area1 = math.pi * radius1**2
area2 = math.pi * radius2**2

pressure = calculate_pressure(force1, area1)
force2 = calculate_force(pressure, area2)

# Display results
st.markdown(f"### Results")
st.write(f"Pressure in the system: `{pressure:.2f} N/m²`")
st.write(f"Force exerted by the large piston: `{force2:.2f} N`")

# Calculate total force based on selected objects
total_object_force = sum(funny_examples[obj] * 9.8 for obj in applied_objects)
st.write(f"Total applied force from selected objects: `{total_object_force:.2f} N`")

# Visualization
st.markdown("### 3D Visualization")

# Create 3D plot
fig = go.Figure()

# Add small piston
fig.add_trace(create_cylinder(x_center=0, y_center=0, z_bottom=0, radius=radius1, height=10, color="blue"))

# Add large piston
fig.add_trace(create_cylinder(x_center=15, y_center=0, z_bottom=0, radius=radius2, height=10, color="red"))

# Add objects on small piston
for i, obj in enumerate(applied_objects):
    fig.add_trace(go.Scatter3d(
        x=[0], y=[0], z=[10 + i],
        mode='markers+text',
        marker=dict(size=5),
        text=obj,
        name=obj
    ))

fig.update_layout(
    scene=dict(
        xaxis=dict(nticks=4, range=[-10, 30]),
        yaxis=dict(nticks=4, range=[-10, 10]),
        zaxis=dict(nticks=4, range=[0, 30]),
    ),
    title="3D Simulation of Pascal's Principle",
)

st.plotly_chart(fig)
