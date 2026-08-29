## Homework 1

**Objective**: Set up a working Python environment for this course (Python + Jupyter +
the imaging libraries) and verify it by completing and running
`lesson_1/homework/Homework.ipynb`.

You only need **one** of the three tracks below. If you already have a working Jupyter
setup, skim Track A for the exact package names and jump to *Verify your environment*.

### Which Python?
Use **Python 3.11, 3.12 or 3.13**. These have prebuilt wheels for every library used
later in the course (TensorFlow, PyTorch, dlib, ultralytics). Python 3.14 also works for
lesson 1, but note that the classic Jupyter Notebook 6.x is incompatible with it, so on
3.14 you must install the modern `notebook` v7 / JupyterLab (see Track A).

---

## Track A — plain virtual environment (recommended)

This is how the course is actually maintained, and it is the lightest option.

```bash
# 1. Create and activate the environment
python3 -m venv ~/venvs/cv           # Windows: py -m venv %USERPROFILE%\venvs\cv
source ~/venvs/cv/bin/activate       # Windows: %USERPROFILE%\venvs\cv\Scripts\activate

# 2. Install the packages used in lesson 1
pip install --upgrade pip
pip install opencv-contrib-python numpy matplotlib pillow ipykernel jupyterlab

# 3. Register this environment as a Jupyter kernel
python -m ipykernel install --user --name cv --display-name "Python (cv)"
```

Notes:
* Install **`opencv-contrib-python`**, not `opencv-python`. Later lessons use the extra
  modules (SIFT in lesson 6, the tracking API in lesson 10) that only ship in the
  `contrib` build. Do not install both — pick one.
* `pillow` is used in lesson 1 for the image-loading comparison; `ipykernel` is what lets
  Jupyter see this environment.
* Each later lesson adds its own dependencies (listed in that lesson's notebooks); install
  them into this same environment as you get there.

---

## Track B — Anaconda / Miniconda

### Step 1
Download an installer:
* **Miniconda** (small, recommended): <https://www.anaconda.com/download/success> — pick
  the Miniconda installer for your OS.
* or the full **Anaconda Distribution**: <https://www.anaconda.com/download> (registration
  is optional; you can skip it).

Licensing note: Anaconda's Terms of Service require a **paid business license** for use
inside organisations with more than 200 employees. Individual, academic and small-team use
of the `conda-forge` channel is free. Miniconda + `conda-forge` avoids the issue entirely.

### Step 2
Install following the prompts. On Windows you can use *Anaconda Navigator*; on
Linux/Mac the command line is simpler.

### Step 3
Create an environment called `cv` and install the packages from `conda-forge`:

```bash
conda create -n cv -c conda-forge python=3.12 \
    opencv numpy matplotlib pillow jupyterlab ipykernel
conda activate cv
python -m ipykernel install --user --name cv --display-name "Python (cv)"
```

(Navigator equivalent: *Environments → Create* → name `cv`, then add `opencv`, `numpy`,
`matplotlib`, `pillow`, `jupyterlab` from the `conda-forge` channel. If OpenCV is not
found, add the channel or run `conda install -n cv -c conda-forge opencv`.)

Avoid mixing the `defaults` and `conda-forge` channels in one environment — it is the most
common cause of a broken conda setup.

##### Optional
Install **Spyder** (`conda install -n cv -c conda-forge spyder`) for editing the `.py`
scripts that some later lessons ship.

---

## Track C — Google Colab

Nothing to install: `cv2`, `numpy`, `matplotlib` and `PIL` are already available. Upload
the lesson's `data/` files (or mount Google Drive) and adjust the paths in the notebook,
since Colab has no local `data/` folder.

---

## Verify your environment

With the environment active, from a terminal:

```bash
python -c "import cv2, numpy, matplotlib, PIL; print('OpenCV', cv2.__version__)"
```

This should print an OpenCV version (4.x) with no `ImportError`.

## Run the homework notebook

1. Launch Jupyter **from inside the `lesson_1/` directory**:
   ```bash
   cd lesson_1
   jupyter lab        # or: jupyter notebook
   ```
   The notebooks load their images with **relative** paths such as
   `cv2.imread('data/kodim21.png')`, so they only work when the working directory is the
   lesson folder.
2. Open `homework/Homework.ipynb` and, if prompted, select the **Python (cv)** kernel.
3. Fill in the blank lines. The notebook asks you to:
   * load an image and convert it to RGB,
   * build a 2×2 collage of the image with its colour channels reordered
     (RGB, RBG, GRB, BGR),
   * build a second collage by flipping the image horizontally and vertically
     (`np.fliplr` / `np.flipud` may help).
4. Run all cells top to bottom with no errors. That is the deliverable.
