# Route-Mapping-and-Location-Tracking
Optimizing Route Mapping and Location Tracking Using Graph Plotting on Latitude-Longitude Coordinates.<br />
This project focuses on creating a mapping and routing mechanism using Python's Folium, Geocoder, and other modules. The primary goal is to generate interactive maps, convert addresses into geographical coordinates, and perform aerial distance calculations.

**Future Prospects:**
1) Implementing SQL to read latitude and longitude data and store necessary information.
2) Developing a Traveling Salesman Algorithm using dynamic programming to find the minimum route that covers all nodes from a base node, while aiming to cover the shortest distance despite the problem being NP-hard.
## Learnings

- **Folium Module:**
  1) Learned to create interactive maps using the Folium module in Python.
  2) Generated maps as separate HTML files.
  3) Embedded and hosted these HTML maps using Python's web browser module.
  <a href="https://pypi.org/project/folium/">Know More About Folium</a>

- **Geocoding:**
  1) Utilized the Geocoder and OpenCage Geocoder libraries for converting addresses into geographical coordinates.
  2) Explored various features and API integrations for accurate location data retrieval.
     <a href="https://pypi.org/project/opencage/">Know More About Geocoding</a>

- **Mathematical Calculations with NumPy:**
  1) Employed NumPy for performing complex mathematical operations.
  2) Calculate the aerial distance between two geographical locations using NumPy functions.
  <a href="https://pypi.org/project/numpy/">Know More About Numpy</a>


- **Web Browser Module:**
  1) Hosted and displayed the generated maps in a web browser directly from the Python script.
  2) Enabled interactive exploration of the generated maps through the web interface.
     <a href="https://docs.python.org/3/library/webbrowser.html">Know More About Webbrowser Module</a>

- **Error Handling and Validation:** Implemented error handling techniques to ensure the application runs smoothly and can handle unexpected inputs gracefully.

- **Project Organization:** Improved skills in structuring a Python project, managing dependencies, and writing clear and concise code documentation.

- ## Installation

This project utilizes the following libraries and modules:

```bash
  pip install phonenumbers
  pip install folium
  pip install pandas
  pip install numpy
  pip install plotly
  pip install gmplot
  pip install opencage
```
Please make sure you have these dependencies installed before running the program.

- ## Key Points

To use OpenCageGeocoder you need to follow these steps:
- Go to their official site and create a account  -> <a href="https://opencagedata.com/">Link</a>
- After creating an account go to the *Geocoding API* section
- And copy your API keys
 <br/>![App Screenshot](https://github.com/mjsonu/Route-Mapping-and-Location-Tracking/blob/main/pic2.png)<br/>
- Then paste it in the following section of the code
  ```bash
  Key="Your API Key"
  geocoder=OpenCageGeocode(Key)
  ```
## Screenshots
Once you run the program on your system a file named *mymap.html* is generated and opens it in your browser <br /> 
Hurray and you just created your first Map and a Routing Mechanism!<br /> <br /> 
![App Screenshot](https://github.com/mjsonu/Route-Mapping-and-Location-Tracking/blob/main/image1.png)<br /> 
And this is how it looks like 😉 <br />
FYI: I am from Kolkata and these are the latitudes and longitudes of my actual alive friends 😅 So, please don't go to their place and disturb them.😂
