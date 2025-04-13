import os

# Print to stdout (these will go to the job log automatically)
print("Hello World from Epsilon SDK!")
print("This is a simple Python script execution test.")

# Create the output directory if it doesn't exist
os.makedirs("output", exist_ok=True)

# Create the output file in the exact location specified in project.yaml
with open("output/hello_world.log", "w") as f:
    f.write("Hello World from Epsilon SDK!\n")
    f.write("This is a simple Python script execution test.\n")