import os

# Print to stdout (this goes to the job log)
print("Hello World from Epsilon SDK!")
print("This is a simple Python script execution test.")

# Create the logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

# Create the output file that matches your project.yaml specification
with open("logs/hello_world.log", "w") as f:
    f.write("Hello World from Epsilon SDK!\n")
    f.write("This is a simple Python script execution test.\n")