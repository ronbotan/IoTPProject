Considerations:
pip install --upgrade imutils
pip install --upgrade opencv-contrib-python
pip install --upgrade numpy
pip install --upgrade flask
pip install --upgrade dlib
pip install --upgrade pickle
pip install --upgrade imageio
pip install --upgrade scypy
pip install --upgrade scikit-learn
pip install --upgrade tensorflow-gpu

1. Run createImage to create images to be used for facetrain
2. Rename the created folder to the name of the user
3. Run the data_preprocess code to process the images for the faces in the frame
4. Run facetrain to create a data model that will be used for facial recognition
5. Run face_recognise to do the facial recognition
6. Run count to do the people counting based on faces in the frame
