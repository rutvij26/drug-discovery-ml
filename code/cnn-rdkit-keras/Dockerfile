FROM continuumio/miniconda3

WORKDIR /app

# Create the environment:
COPY environment.yml .
RUN conda env create -f environment.yml

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "cnn-rdkit-keras-env", "/bin/bash", "-c"]

# Demonstrate the environment is activated:
RUN echo "Make sure numpy is installed:"
RUN python -c "import numpy"

# The code to run when container is started:
COPY run.py .
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "cnn-rdkit-keras-env", "python", "run.py"]
