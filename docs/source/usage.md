# Edit This Website

## Steps to Edit the Website on terminal

1. **Clone the `Josefowicz_lab_wiki` repository and enter the directory**:
   ```bash
   git clone [https://github.com/YourUsername/Josefowicz_lab_wiki.git](https://github.com/ReshmaRamaiah10/Josefowicz_lab_wiki.git)
   cd Josefowicz_lab_wiki
   ```

2. **Create a Conda Environment (manually)**:
   ```bash
   conda create -n myenv python=3.8
   ```

3. **Activate the Environment**:
   ```bash
   conda activate myenv
   ```

4. **Install Dependencies**:
   Use pip to install any required packages, including those specified in your `requirements.txt`:
   ```bash
   pip install -r docs/requirements.txt
   ```

5. **Install the Tool**:
   If you haven't installed `sphinx-autobuild`, you can do so using pip:
   ```bash
   pip install sphinx-autobuild
   ```

6. **Run the Local Server**:
   Navigate to the directory where your `conf.py` file is located and run:
   ```bash
   sphinx-autobuild . _build/html
   ```
```
