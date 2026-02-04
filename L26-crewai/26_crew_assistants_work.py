# Title: Use Local Ollama LLM with CrewAI
#
# Description:
# This script introduces "CrewAI", a framework for orchestrating "AI Agents".
# Unlike a simple Chatbot (User <-> AI), CrewAI allows you to define:
# 1. AGENTS: AI personas with specific roles (e.g., Researcher, Writer).
# 2. TASKS: Specific jobs those agents must complete.
# 3. CREW: The team structure that manages how agents work together.
#
# This example creates a simple 1-Agent crew to demonstrate the syntax.
#
# Installation:
# pip install streamlit crewai langchain-community
#
# How to run:
# streamlit run 25.py

import streamlit as st
from crewai import Agent, Task, Crew, LLM  # The 3 core building blocks of CrewAI

st.title("Use Local Ollama LLM with CrewAI")

# Input for the user's request
prompt = st.text_area(label="Enter your prompt:")
button = st.button("Generate")

if button:
    if prompt:
        # --- Step 1: Define the Agent ---
        # An Agent is an autonomous unit. It needs:
        # - role: What is its job title?
        # - goal: What is it trying to achieve?
        # - backstory: Context about its personality or expertise (helps the LLM roleplay).
        # - llm: Which model drives its brain? Note the syntax "ollama/modelname".
        # llm = LLM(model='ollama/llama3.3', base_url= 'http://localhost:11434')
        
        # GPT OSS LLM - spins up a lot of compute 
        llm = LLM(
        model="gpt-oss:latest",
        base_url="http://localhost:11434/v1",
        api_key="ollama"
        )
        agent = Agent(
            role="Assistant",
            goal="Provide helpful responses based on user input.",
            backstory="This agent assists users by generating responses using a local Ollama LLM.",
            # llm="ollama/llama3.3"  # Crucial: Connects CrewAI to your local Llama 3 model
            llm=llm  # Crucial: Connects CrewAI to your local Llama 3 model
        )

        # --- Step 2: Define the Task ---
        # A Task is a specific unit of work. It needs:
        # - description: Instructions on what to do.
        # - expected_output: A definition of what the result should look like (text, list, etc.).
        # - agent: Which agent is responsible for this task?
        task = Task(
            description=f"Generate a response based on user input: {prompt}",
            expected_output="The generated response will be a flat text.",
            agent=agent  # Link the Task to the Agent
        )

        # --- Step 3: Define the Crew ---
        # The Crew is the container that holds agents and tasks together.
        # It manages the workflow (e.g., sequential execution).
        crew = Crew(agents=[agent], 
                    model='gpt-oss:latest',
                    tasks=[task])

        # --- Step 4: Kickoff ---
        # Start the process. The agents will begin working on their tasks.
        # This returns the final output of the last task.
        result = crew.kickoff()

        # Display the result
        st.markdown(result)
        
''' Sample Input : 
    What is real
'''
'''Output: (Pretty large!)
The question “What is real?” is one of the oldest and most profound inquiries in philosophy, science, and everyday human experience. It intersects with ontology (the study of being), epistemology (the study of knowledge), and even aesthetics. While there is no single definitive answer that satisfies every perspective, here are several major approaches that together paint a richer picture of what “real” might mean.

1. The Philosophical Tradition
a. Metaphysical Realism
Metaphysical realism claims that there exists a world independent of our minds and perceptions. According to this view:

Physical Objects: The table in your living room, the tree outside, and the atoms within them truly exist, regardless of whether anyone observes them.
Objective Properties: Properties like mass, color, and spatial relationships are not merely abstractions; they are embedded in the fabric of reality.
b. Idealism
Idealism proposes that reality is fundamentally constituted by consciousness or ideas:

Solipsism: Only my mind is certain to exist; the external world may be a projection or dream.
Absolute Idealism (Hegel): The Absolute spirit or mind is the underlying reality that gives rise to both the physical world and consciousness.
c. Phenomenology
Phenomenology looks at reality through the lens of lived experience:

Intentionality: All consciousness is directed toward something; what we say “exists” is always in relation to how it is experienced.
Bracketing: Phenomenologists ask us to “epoché” or set aside judgments about existence to investigate pure experience first-hand.
d. Anti‑Realism / Constructivism
Anti-realists argue that what we consider “real” is a construction (scientific, cultural, or linguistic):

Scientific Realism vs. Instrumentalism: Scientists may treat the electron or quark as “real” objects by their predictive utility, but some philosophers argue they are merely useful fictions.
Social Constructivism: Realities like gender, race, or money are socially fabricated but have real effects because we agree on them.
2. Science’s View
a. Empirical Reality
Science investigates a reality that can, in principle, be observed and measured. The key features:

Empirical Evidence: Laws of physics are formulated based on experiments that reproducibly describe phenomena.
Objectivity: Scientific facts are supposed to be independent of the observer’s beliefs.
b. The Role of Models
Even in science, the most refined models (e.g., quantum field theory) are not the "real thing" per se; they are extremely successful approximations:

Theory vs. Reality: Our best theories are always provisional; they may someday be superseded by deeper explanations.
Measurement Problem: In quantum mechanics, the act of measuring seems to affect reality. The many interpretations (Copenhagen, many-worlds, Bohmian mechanics) each offer a different stance on what constitutes reality at the smallest scales.
3. Everyday Reality
For most practical purposes, “real” means:

It has observable consequences: You can touch a cup, see a car, feel the warmth of sunlight.
It persists through time: It isn’t a fleeting hallucination but something that exists and can change over time.
It engages multiple senses: When we perceive an object, it often engages sight, touch, sound, etc., reinforcing the notion that it is real.
Even in this everyday sense, philosophy reminds us that our perceptions are filter processes; our brains construct a model of the world that may differ from the “world-in-itself.” Yet, the model is useful enough to navigate, predict, and survive.

4. A Cross‑Disciplinary Outlook
A balanced view draws on multiple traditions:

Physical Reality: The world exists independent of us, but our human perspective is one among many ways it can be understood or modeled.
Cognitive Reality: We have mental representations and experiences that are themselves real to us; they shape how we interact with the world.
Social Reality: Constructs like laws and language create structures that have tangible impacts.
This triad reflects a pragmatic approach: we accept that we can’t fully access the “ultimate” reality in one universal way, but we can still navigate and manipulate the world based on our best understandings.

5. Summary
Real is a multifaceted concept that depends on the epistemic lens we apply.
Metaphysical Realism posits an objective world; Idealism grounds reality in consciousness; Phenomenology focuses on lived experience.
Science provides empirical models of a real, measurable universe, yet models are approximations.
On a day‑to‑day level, real objects and events are those that reliably affect us across multiple senses.
Finally, reality may be best understood as a multi‑layered construct where objective facts, mental models, and social agreements all coexist and interact.
In short, what is “real” can be seen as both something that exists independently of us and something that is also profoundly shaped by how we observe, think, and communicate about it. The question invites constant reflection, and each philosophical or scientific discipline offers a useful viewpoint.
'''
