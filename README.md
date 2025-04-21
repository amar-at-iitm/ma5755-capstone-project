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

## How to Start the Project (For All Teammates)

### Step 1: Clone the Repository
```bash
git clone https://github.com/amar-at-iitm/ma5755-capstone-project.git
cd ma5755-capstone-project
```

### Step 2: Build the Docker Image (One-Time Only)
```bash
docker build -t capstone-project .
```

### Step 3: Run Docker Container
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
### Step 4: Run Python Script Inside Container
```bash
python scripts/data_download.py
```

### Step 5: Exit the Container
```bash
exit
```

---

## Project Folder Structure
```
ma5755-capstone-project/
├── data/
│   └── raw/                  # Raw data CSVs are saved here
├── scripts/
│   └── data_download.py      # Script to download data from Google Drive
├── Dockerfile                # Docker setup
├── requirements.txt          # Python dependencies
├── README.md                 # Project instructions (this file)
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

---


