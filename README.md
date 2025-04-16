# ScrapeJobs
scrape jobs

To run the Flask application provided in the code, follow these steps:

# Prerequisites
Install Python: Ensure Python is installed on your system. You can download it from python.org.
Install Required Libraries: Install the necessary Python libraries (Flask, requests, and beautifulsoup4) using pip.

Steps to Run the Program
#Open a Terminal:

cd  c:\Users\repo

On Windows, you can use Command Prompt, PowerShell, or the terminal in Visual Studio Code.
Navigate to the File Directory: Use the cd command to navigate to the directory where app.py is located:

Install Dependencies: Run the following command to install the required libraries:
pip install flask requests beautifulsoup4


Run the Flask Application: Execute the Python script using the following command:
python app.py

Access the Application:
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)


Once the application is running, you will see output similar to:
Open a web browser and navigate to http://127.0.0.1:5000/scrape_jobs.

Test the Endpoint:
http://127.0.0.1:5000/scrape_jobs?keywords=data+scientist&location=New+York

You can pass query parameters like keywords and location in the URL. For example:
Notes
If you encounter any errors, ensure all dependencies are installed and the Python version is compatible (Python 3.x is recommended).
Use CTRL+C in the terminal to stop the Flask server when you're done.### Notes
If you encounter any errors, ensure all dependencies are installed and the Python version is compatible (Python 3.x is recommended).
Use CTRL+C in the terminal to stop the Flask server when you're done.
