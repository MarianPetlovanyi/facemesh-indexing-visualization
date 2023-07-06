import cv2
import mediapipe as mp
import plotly.graph_objects as go

# Load the image
image_path = "face.jpg"
image = cv2.imread(image_path)

# Flip the image vertically
#image = cv2.flip(image, 0)

# Convert the image to RGB format
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Initialize the MediaPipe FaceMesh model
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()
print(image.shape[0], image.shape[1])
# Process the image and extract the face landmarks
results = face_mesh.process(image)
if results.multi_face_landmarks:
    fig = go.Figure(data=[go.Image(z=image)])

    for face_landmarks in results.multi_face_landmarks:
        x_coords = []
        y_coords = []
        for landmark in face_landmarks.landmark:
            x = int(landmark.x * image.shape[1])
            y = int(landmark.y * image.shape[0])
            x_coords.append(x)
            y_coords.append(y)


        fig.add_trace(go.Scatter(
            x=x_coords,
            y=y_coords,
            mode='markers',
            marker=dict(size=2, color='lime'),
            line=dict(color='lime', width=2),
        ))

    fig.update_layout(
        showlegend=False,
        xaxis=dict(visible=False, range=[0, image.shape[1]]),
        yaxis=dict(visible=False, range=[0, image.shape[0]], autorange = 'reversed')

    )
    for trace in fig.data:
        trace.hovertemplate = "Index: %{pointNumber}"
    fig.show()
else:
    print("No face landmarks detected.")

