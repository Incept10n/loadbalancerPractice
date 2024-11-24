# Step 1: Use an official Python runtime as a parent image
FROM python:3.11-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy the current directory contents into the container at /app
COPY . /app

# Step 4: Install any necessary dependencies
RUN pip install fastapi[standard]

# Step 5: Expose the port the app runs on
EXPOSE 8000

# Step 6: Command to run the application
CMD ["fastapi", "run", "server1.py", "--port", "8000"]
