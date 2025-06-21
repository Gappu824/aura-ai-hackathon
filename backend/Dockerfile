# Stage 1: Build the dependencies using a generic Python image
FROM python:3.9-slim as builder
WORKDIR /opt/
COPY requirements.txt .

# Install dependencies from requirements.txt INSIDE the Linux container
RUN pip install --upgrade pip && \
    pip install -r requirements.txt -t ./python

# Stage 2: Create the final, optimized image using the official AWS base image
FROM public.ecr.aws/lambda/python:3.9

# Set the working directory that Lambda uses
WORKDIR /var/task

# Copy the installed dependencies from the builder stage
COPY --from=builder /opt/python ./

# Copy your application code
COPY app/ ./app
COPY handler.py .

# Set the command that tells the Lambda runtime how to start the handler
CMD ["handler.handler"]