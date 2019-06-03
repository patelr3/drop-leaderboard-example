FROM allennlp/allennlp:v0.8.3

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
    
WORKDIR /local

# Copy select files needed for installing requirements.
# We only copy what we need here so small changes to the repository does not trigger re-installation of the requirements.
COPY requirements.txt .
#COPY install_requirements.sh .
COPY predict.py .
COPY run_model.sh .
COPY drop_library ./drop_library
COPY drop_dataset_dev.json . 
#RUN ./install_requirements.sh

# EXPOSE 8000
ENTRYPOINT ["/bin/bash"]
#Cmd ["/bin/bash"]
