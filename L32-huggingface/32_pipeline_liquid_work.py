from transformers import pipeline
pipe = pipeline("text-generation", model="LiquidAI/LFM2.5-1.2B-Thinking")
messages = [ 
    {"role" : "user", "content" : "What is the Sonic Boom in Aviation?"},  
]
output = pipe(
    messages,
    max_new_tokens=5024,
    do_sample=True,
    temperature=0.7,
    top_k=50,
    top_p=0.5)
# Nucleus sampling for better quality

# The result is a complex list structure. We access [0]['generated_text'] to get the answer.
# We access [1]['content'] to get content from that object
# We then need to get content that comes after </think>

print(output[0]['generated_text'][1]['content'].split("</think>")[1])


# Potential output
# The **Sonic Boom** in aviation refers to the sudden, 
# loud shockwave generated when an aircraft travels faster than the speed of sound.