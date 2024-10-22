Edit the Website on Terminal
=============================

1. **Clone the `Josefowicz_lab_wiki` repository**:
   You can clone the repository using the following command:
   ::
   
      git clone https://github.com/YourUsername/Josefowicz_lab_wiki.git
      cd Josefowicz_lab_wiki

2. **Create a Conda Environment (manually)**:
   ::
   
      conda create -n sphinx_env python=3.8

3. **Activate the Environment**:
   ::
   
      conda activate sphinx_env

4. **Install Dependencies**:
   Use pip to install any required packages, including those specified in your `requirements.txt`:
   ::
   
      pip install -r docs/requirements.txt

5. **Install the Tool**:
   If you haven't installed `sphinx-autobuild`, you can do so using pip:
   ::
   
      pip install sphinx-autobuild

6. **Run the Local Server**:
   Navigate to the directory where your `conf.py` file is located and run:
   ::
   
      sphinx-autobuild . _build/html

   After running the command, you should see output indicating that the server is running. It usually shows a message like:
   ::
   
      > Server is running on http://127.0.0.1:8000/

   Open your web browser and navigate to that URL (typically `http://127.0.0.1:8000/`) to view your documentation.

.. Automatic Reload::

   One of the benefits of using ``sphinx-autobuild`` is that it automatically rebuilds your documentation whenever you make changes to the source files. You can just save your changes, and the browser will refresh to show the updated content.
