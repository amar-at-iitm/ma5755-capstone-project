# MA5755-capstone-project: Drought & Rainfall Impact Analysis
Objective: Assess the impact of changing rainfall patterns on crop productivity over decades on the TCI-ICRISAT District Database (571 districts, 1966-2017).

- [ICRISAT District-level dataset](http://data.icrisat.org/dld/index.html)
- [india_district.geojson](https://drive.google.com/file/d/1N-rz3VugxTZYrrru5AmtE2oMBDsH2zDZ/view?usp=sharing) is used for the district map

---

## Project Setup (Using Docker)

### Prerequisites (Install Once)
- Docker: [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)
- VS Code Extensions:
  - Docker
  - Python

---
## Project Folder Structure
```
ma5755-capstone-project/
├── data/
    └── raw/                                # Raw data CSVs are saved here
    └── cleaned/                            # cleaned files
    └── india_district.geojson              # District map
├── scripts/
    └── data_download.py                    # Script to download data from Google Drive
    └── ML.ipynb                            # Model Training Notebook
    └── data_cleaning.ipynb                 # Data Cleaning Notebook
    └── eda_analysis.ipynb                  # EDA Notebook
    └── data_cleaning_and_merged.py         # Supporting file for streamlit
    └── combined_rainfall_yield_dashboard.py # streamlit dashboard
├── Dockerfile                              # Docker setup
├── docker-compose.yml                      # Docker Compose file
├── definitions.pdf                         # Some important terms used in the datasets
├── units.pdf                               # Units used in the datasets
├── requirements.txt                        # Python dependencies
├── README.md                               # Project instructions (this file)
```

## How to Start the Project 

### Step 1: Clone the Repository
```bash
git clone https://github.com/amar-at-iitm/ma5755-capstone-project.git
cd ma5755-capstone-project
```

### Step 2: Build the Docker Image (One-Time Only)
```bash
docker-compose build
```
Build a Specific Container
```bash
docker compose build <container_name>
```
### Run the complete Docker Setup 
```bash
docker-compose up
```
Go to 
1. http://localhost:8888
   - For all the notebook files
3. http://localhost:8501
   - For the Streamlit app dashboard

Run a specific container
```bash
docker-compose up <container_name>
```

### Run Docker Container
This mounts your current folder into the Docker container and gives you a terminal:
For Linux/Mac
```bash
docker run -it --rm -v "$PWD":/app capstone-project bash
```
For Windows Command Prompt
```cmd
docker run -it --rm -v %cd%:/app capstone-project bash
```
For Windows PowerShell
```powershell
docker run -it --rm -v ${PWD}:/app capstone-project bash
```
#### Run Python Script Inside Container
```bash
python scripts/data_download.py
```
```bash
python scripts/combined_rainfall_yield_dashboard.py
```

#### Exit the Container
```bash
exit
```
---

## Dependencies
All dependencies are listed in `requirements.txt` and are installed inside the Docker container.

---
### Run Specific Part
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
- Run rainfall_yield_app.py
- Start the streamlit app
- Accessible at: http://localhost:8501


## Work Done Till Now
- [x] Docker setup complete
- [x] Data download script written
- [x] Folder structure organised
- [x] GitHub repository ready for collaboration
- [x] ML model
- [x] Interactive dashboard
- [x] Report

---


