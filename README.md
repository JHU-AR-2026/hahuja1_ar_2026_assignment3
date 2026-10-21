# Assignment 3, Introduction to Augmented Reality

Harsh Ahuja (JHED: hahuja1)
EN.601.654/454 Introduction to Augmented Reality, Fall 2026, Johns Hopkins University

This repo has my code for the programming parts of Assignment 3. Each folder matches a question from the assignment.

## Repository layout

```
Q2/
  q2_webxr_scene.html          WebXR AR scene (Babylon.js)
  assets/of_planes_and_satellites.glb
Q3e/
  q3e_projection.py            projection matrix and camera-to-pixel mapping
Q4/
  4a.js                        custom shader, one point light (Playground code)
  4c.js                        custom shader, two point lights (Playground code)
  index.html                   standalone page running the 4c scene
```

## Q2: WebXR hit-test scene

An immersive AR scene built with Babylon.js. The right controller casts a hit-test ray against real surfaces, and pulling the right trigger places the glTF model at the hit point. After that you can move, rotate and scale the most recently placed model with the controllers. The button mapping assumes Meta Quest controllers.

Controls:

- Right trigger places a new copy of the model where the right controller's ray hits a surface.
- Right thumbstick moves the model along the floor plane.
- A scales the model up by 10%, and B scales it down by 10%.
- Left thumbstick (left/right) rotates the model around its vertical axis.
- X resets the model to the position, rotation and scale it had when it was placed.

### How to run

WebXR only works in a secure context (HTTPS or `localhost`), and the model is loaded with a relative path, so opening the HTML file straight from disk will not work. Serve the `Q2` folder and open it in the Quest browser:

```bash
cd Q2
python3 -m http.server 8000
```

With the headset connected over USB and developer mode on, forward the port so the headset can reach it as `localhost`:

```bash
adb reverse tcp:8000 tcp:8000
```

Then open `http://localhost:8000/q2_webxr_scene.html` in the Meta Quest Browser and press the AR button in the bottom right corner. Hosting the folder on any HTTPS server works too.

## Q3e: Projection matrix

`q3e_projection.py` builds the OpenGL-style perspective projection matrix from the image size, near/far planes, focal lengths and principal point. It then takes a point in camera coordinates through clip space and normalized device coordinates to a pixel location, printing each step.

### How to run

Needs Python 3 and NumPy.

```bash
pip install numpy
python3 Q3e/q3e_projection.py
```

The input values are set in the `__main__` block at the bottom of the file (800x600 image, n = 0.2, f = 20, fx = fy = 800, principal point (400, 400), point (0.3, -0.15, -6)). Change them there to try other inputs.

## Q4: Custom Phong shaders

Both scenes put a sphere and a cylinder in front of a free camera and shade them with a custom GLSL `ShaderMaterial` instead of Babylon's built-in materials. The fragment shader computes ambient, diffuse and specular (Phong) terms per point light with inverse-square attenuation.

- `4a.js` uses a single point light.
- `4c.js` adds a second, magenta-tinted point light on the other side of the scene and sums the two contributions.

### How to run

For `4a.js` or `4c.js`, open the [Babylon.js Playground](https://playground.babylonjs.com/), replace the default code with the contents of the file and press Run.

`index.html` is the 4c scene wrapped in a full HTML page. It loads Babylon.js from the CDN and has no local assets, so you can open it directly in a browser. Drag with the mouse to look around and use the arrow keys to move the camera.
