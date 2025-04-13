import os

# Print to stdout (this goes to the job log)
print("Hello World from Epsilon SDK!")
print("This is a simple Python script execution test.")

# Create the output directory if it doesn't exist
os.makedirs("output", exist_ok=True)

# Create the output file that matches your project.yaml specification
with open("output/hello_world.log", "w") as f:
    f.write("Hello World from Epsilon SDK!\n")
    f.write("This is a simple Python script execution test.\n")