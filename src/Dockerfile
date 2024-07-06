FROM ollama/ollama:latest

# Copy the configuration file and shell script into the container
COPY Modelfile /usr/local/bin/Modelfile
COPY start-ollama.sh /usr/local/bin/start-ollama.sh

# Ensure the shell script is executable
RUN chmod +x /usr/local/bin/start-ollama.sh
RUN chmod +x /usr/local/bin/Modelfile

# Expose the port
EXPOSE 11434
