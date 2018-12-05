from subprocess import Popen
print("hi")
Popen(['python', 'test.py'])  # something long running
# ... do other stuff while subprocess is running
Popen(['python', 'test2.py'])

print("New Hello")

