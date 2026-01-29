import io
import sys

old_stdout = sys.stdout
sys.stdout = buffer = io.StringIO()

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

sys.stdout = old_stdout
output = buffer.getvalue()
print(output)
# print('The output is:', output)