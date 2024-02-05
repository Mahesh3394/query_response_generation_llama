# Use the official Python image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file first to leverage Docker cache
COPY requirements.txt .

# Install required Python packages
RUN pip install -r requirements.txt

# Copy the rest of the application files to the container's working directory
COPY . .


# Command to run your Streamlit application
CMD ["python", "app.py"]
