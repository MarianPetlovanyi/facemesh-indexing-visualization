import argparse
import cv2
import mediapipe as mp
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import mplcursors

mp_face_mesh = mp.solutions.face_mesh.FaceMesh()

parser = argparse.ArgumentParser(description='Plotting tool')
parser.add_argument('--plot-library', choices=['matplotlib', 'plotly'], default='matplotlib', help='Choose the plot library (matplotlib or plotly)')
args = parser.parse_args()

image_path = './face.jpg'
image = cv2.imread(image_path)

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

results = mp_face_mesh.process(image_rgb)
face_landmarks = results.multi_face_landmarks[0].landmark

x = []
y = []
z = []
landmarks_px = []
for landmark in face_landmarks:
    x.append(landmark.x)
    y.append(landmark.y)
    z.append(landmark.z)


if args.plot_library == 'matplotlib':
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    scatter = ax.scatter(x, y, z)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    mplcursors.cursor(hover=True).connect("add", lambda sel: sel.annotation.set_text(f"Index: {sel.target.index}"))
    plt.show()

elif args.plot_library == 'plotly':
    fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers', marker=dict(size=2))])
    fig.update_layout(scene=dict(xaxis_title='X Label', yaxis_title='Y Label', zaxis_title='Z Label'))

    fig.show()
