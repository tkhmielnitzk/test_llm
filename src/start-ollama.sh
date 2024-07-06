#!/bin/sh

# Start the Ollama server
echo "Starting the Ollama server..." 
ollama serve &

# Get the process ID of the server
SERVER_PID=$!

# Wait to ensure the server has started
sleep 10

# Check if the server is running
echo "Ollama server is running."

# Create the model description
ollama create description_immo -f /usr/local/bin/Modelfile

# Check if the model was created successfully
if [ $? -eq 0 ]; then
    echo "Model created successfully."
    sleep 5
    # Run the model
    ollama run description_immo
else
    echo "Failed to create the model."
    kill $SERVER_PID
    exit 1
fi

# Wait for the server process to finish
wait $SERVER_PID

