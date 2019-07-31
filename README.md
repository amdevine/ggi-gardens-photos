Download GGI Gardens Photos from iNaturalist
==============================================

This repository contains Python code (as a script and as a Jupyter notebook) to automate downloading GGI-Gardens photos and data from iNaturalist.

iNaturalist Observation Data
------------------------------

In order to run this code, a CSV export of GGI-Gardens observation data is needed from iNaturalist. Instructions to get this export are as follows:

1. Log into iNaturalist


2. Once logged in, you should be able to use this link to get to the **Export Observations** page for the Global Genome Initiative Gardens project: https://www.inaturalist.org/observations/export?projects%5B%5D=global-genome-initiative-gardens (Alternatively, click the **Projects** tab, then **Global Genome Initiative Gardens**, then scroll down and click **Export Observations**.)


3. In Section 1 (Create a Query), find the **Filter** options and select the box for **w/ photos**. 


4. In Section 3 (Choose columns), ensure that the **id** box in the **Basic** section is selected.


5. Add additional filters and select/deselect additional columns based on the observation data you would like to export.


6. Scroll down to the bottom and click **Create export**. You can either wait a few minutes for the report to generate, or choose to receive a notification email.  


7. Once the report is generated, download it and extract the .csv file from the zip archive. Rename the extracted file `observations.csv`.


Running the Python code
------------------------

### Installing Python via the Anaconda distribution

To run the Python code, you will need a version of Python 3 installed on your computer. (If you do not have Python 3 installed, you can get it through the [Anaconda Python 3.x distribution](https://www.anaconda.com/distribution/))

If you have installed Python with the Anaconda distribution, you should have all the required Python libraries to run this code. If you have installed Python through another distribution, you may need to install the `pandas` and `requests` libraries. This can be done from the command line/terminal with `pip install pandas` and `pip install requests`.

### Code files

Either the **Jupyter notebook** or the **script file** should be saved in the same folder as `observations.csv`. The downloaded images will take up several gigabytes of disk space, so it is recommended that this folder be in a location that has sufficient storage. (A Dropbox folder shared with many other users is not recommended.)

### Jupyter notebook

If you installed Python with the Anaconda distribution, Jupyter will automatically be installed on your computer. To access the Jupyter notebook, open a command line/terminal console and run `jupyter notebook`. This will open a browser-based GUI interface that you can use to navigate to and open the notebook.

To execute the code, use the **Run** button at the top to run cells one by one. You can also use the Shift+Enter keyboard shortcut.

### Python script

To run the Python script, open a command line/terminal window and type the following command:

`python download_inaturalist_images.py`

(if you're on a Mac, you may need to use `python3 download_inaturalist_images.py`)
