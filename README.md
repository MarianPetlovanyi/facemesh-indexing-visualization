## Installation

1. Make sure you have [Python](https://www.python.org/) installed on your system.

2. Clone the repository or download the program files to your local machine.

3. Open a terminal or command prompt and navigate to the program directory.

4. Create a new virtual environment:

   - For Windows:
     ```shell
     python -m venv face-landmarks-env
     ```

   - For Linux and macOS:
     ```shell
     python3 -m venv face-landmarks-env
     ```

   Activate the environment:

   - For Windows:
     ```shell
     face-landmarks-env\Scripts\activate
     ```

   - For Linux and macOS:
     ```shell
     source face-landmarks-env/bin/activate
     ```

5. Install the required packages using the following command:

   ```shell
   pip install -r requirements.txt
   ```

   This will install the necessary packages specified in the `requirements.txt` file, including Mediapipe, OpenCV, Matplotlib, and Plotly.

6. Download an image that contains a face and save it in the same directory as the program files. Rename the image as `face.jpg` (or update the `image_path` variable in the code with the correct file path).

## Usage

To run the program, use the following command:

```shell
python main.py --plot-library [library]
```

Replace `[library]` with either `matplotlib` or `plotly` to choose the plotting library.

For example, to visualize the face landmarks using Matplotlib, run:

```shell
python main.py --plot-library matplotlib
```

To visualize the face landmarks using Plotly, run:

```shell
python main.py --plot-library plotly
```

The program will display a 3D plot showing the face landmarks detected in the image. You can interact with the plot by rotating it or zooming in/out.

If you selected Matplotlib as the plotting library, you can hover over each point to see its index.

To exit the program, simply close the plot window.

Remember to deactivate the virtual environment after you are done using the program:

```shell
deactivate
```

That's it! You can now visualize face landmarks using the Face Landmarks Visualization program.