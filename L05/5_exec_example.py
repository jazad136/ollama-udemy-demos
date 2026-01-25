code = """
import random
print(random.randint(0,10))
"""
# exec(code)


try:
    # exec("""print("Hello")""")
    exec(code)
except Exception as e:
    print(f"Error executing generated code: {e}")
