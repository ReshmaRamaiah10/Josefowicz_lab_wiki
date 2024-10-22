# Edit the Website on terminal

1. **Clone the `Josefowicz_lab_wiki` [repository](https://github.com/ReshmaRamaiah10/Josefowicz_lab_wiki) and enter the directory**:
   ```bash
   git clone https://github.com/YourUsername/Josefowicz_lab_wiki.git
   cd Josefowicz_lab_wiki
   ```

2. **Create a Conda Environment (manually)**:
   ```bash
   conda create -n sphinx_env python=3.8
   ```

3. **Activate the Environment**:
   ```bash
   conda activate sphinx_env
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
   After running the command, you should see output indicating that the server is running. It usually shows a message like:
   ```arduino
   > Server is running on http://127.0.0.1:8000/
   ```
   Open your web browser and navigate to that URL (typically `http://127.0.0.1:8000/`) to view your documentation.

Automatic Reload
One of the benefits of using `sphinx-autobuild` is that it automatically rebuilds your documentation whenever you make changes to the source files. You can just save your changes, and the browser will refresh to show the updated content.
