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
## Project Folder Structure
```
ma5755-capstone-project/
├── data/
    └── raw/                  # Raw data CSVs are saved here
    └── cleaned/              # cleaned files
  └── india_district.geojson # District map
├── scripts/
    └── data_download.py      # Script to download data from Google Drive
    └── data_cleaning_and_merged.py # Supporting file
    └── combined_rainfall_yield_dashboard.py # streamlit dashboard
├── Dockerfile                # Docker setup
├── requirements.txt          # Python dependencies
├── README.md                 # Project instructions (this file)
```

## How to Start the Project 

### Step 1: Clone the Repository
```bash
git clone https://github.com/amar-at-iitm/ma5755-capstone-project.git
cd ma5755-capstone-project
```

### Step 2: Build the Docker Image (One-Time Only)
```bash
docker build -t capstone-project .
```
Build Specific Container
```bash
docker compose build <container_name>
```
### Run the complete docker 
```bash
docker-compose up
```
Go to 
1. http://localhost:8888
   - For all the notebook files
3. http://localhost:8501
   - For the Streamlit app dashboard

Run specific container
```bash
docker-compose up <container_name>
```

### Run Docker Container
This mounts your current folder into the Docker container and gives you a terminal:
For linux/mac
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

## Work Done Till Now
- [x] Docker setup complete
- [x] Data download script written
- [x] Folder structure organized
- [x] GitHub repository ready for collaboration
- [x] Interactive dashboard

---


