# MA5755-capstone-project: Drought & Rainfall Impact Analysis
Objective: Assess the impact of changing rainfall patterns on crop productivity over decades on the TCI-ICRISAT District Database (571 districts, 1966-2017).

ICRISAT District-level dataset
link:- http://data.icrisat.org/dld/index.html

---

## Project Setup (Using Docker)

### Prerequisites (Install Once)
- Docker: [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)
- VS Code Extensions:
  - Docker
  - Python

---
- Link for india_district.geojson because it is more than 25Mb, unable to upload, download it from here: [https://drive.google.com/file/d/1N-rz3VugxTZYrrru5AmtE2oMBDsH2zDZ/view?usp=sharing]
---
## Project Folder Structure
```
ma5755-capstone-project/
├── data/
│   └── raw/                     # Raw data CSVs are saved here
│   └── cleaned/                 # Raw data CSVs are saved here

├── scripts/
│   ├── data_download.py         # Script to download data from Google Drive
│   ├── data_cleaning.ipynb      # 
│   └── eda_analysis.ipynb       # 
│   └── data_cleaning_and_merge.py  
│   └── rainfall_yield_app.py       
|   └──district_map_dashboard.py 
│   └── combined_rainfall_yield_dashboard.py # it requires india_district.geojson file I have uploaded, please check it should be in the same folder.
          
├── Dockerfile                   # Docker setup
├── docker-compose.yml           # Docker Compose file
├── requirements.txt             # Python dependencies
├── Readme.md                    # Project instructions (this file)

```
---
## Steps to Start the Project 

### Step 1: Clone the Repository
```bash
git clone https://github.com/amar-at-iitm/ma5755-capstone-project.git
cd ma5755-capstone-project
```

### Step 2: Build the Docker Image (One-Time Only)
```bash
docker build -t capstone-project .
```
#### To build specific container
```bash
docker-compose build <container_name>
```
### Step 3: Run Specific Part
#### Get Data
```bash
docker-compose up get_data
```

#### Run The Notebook
```bash
docker-compose up jupyter_notebook
```
It will:
- Start Jupyter in /app/scripts
- Show all .ipynb notebooks
- Be accessible at: http://localhost:8888

#### Run The Streamlit App
```bash
docker-compose up streamlit-app
```
It will:
- Run rainfall_yeild_app.py
- Start the streamlit app
- Accessible at: http://localhost:8501
  
## Run Docker Container
This mounts the current folder into the Docker container and gives a terminal:
For linux/mac
```bash
docker run -it --rm -v "$PWD":/app capstone-project bash
```
For Windows Command Prompt
```cmd
docker run -it --rm -v %cd%:/app capstone-project bash
```
For Windows PowerShell
```PowerShell
docker run -it --rm -v ${PWD}:/app capstone-project bash
```
#### Run Python Script Inside Container
```bash
python scripts/data_download.py
```
```bash
python scripts/rainfall_yeild_app.py
```

#### Exit the Container
```bash
exit
```
---


Download the Merged dataset file from the cleaning and merging script, and keep both files in one folder.
In your terminal, from the folder containing rainfall_yield_app.py, combined_rainfall_yield_dashboard.py, merged_dataset.csv, india_district.geojson, district_map_dashboard.py run "streamlit run rainfall_yield_app.py" and "streamlit run district_map_dashboard.py", you can separately view, or else only run "streamlit run combined_rainfall_yield_dashboard.py" for both

---

## Dependencies
All dependencies are listed in `requirements.txt` and are installed inside the Docker container.

---

## Work Done Till Now
- [x] Docker setup complete
- [x] Data download script written
- [x] Folder structure organized
- [x] GitHub repository ready for collaboration
- [x] Data Cleaning
- [x] Interactive dashboard
---


