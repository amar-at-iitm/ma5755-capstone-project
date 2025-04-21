import os
import gdown

# Making sure this directory exists
os.makedirs("data/raw", exist_ok=True)

# File IDs from Google Drive
files = {
    "area_production_yield_data.csv": "1RKcWF30zOn2il99fPLB4lQPqeC7ZDNfB",
    "monthly_rainfall_data.csv": "1zZ2w59Avbm8uqV_97hDRcdNcicXS06aS",
    "normal_rainfall_data.csv": "1hM76osh-LVPL7oQcEZvpX9DhfZ0qBHx3"
}
# google drive links of all the three data
#https://drive.google.com/file/d/1RKcWF30zOn2il99fPLB4lQPqeC7ZDNfB/view?usp=sharing
#https://drive.google.com/file/d/1zZ2w59Avbm8uqV_97hDRcdNcicXS06aS/view?usp=sharing
#https://drive.google.com/file/d/1hM76osh-LVPL7oQcEZvpX9DhfZ0qBHx3/view?usp=sharing


# Download each file only if not already present
for filename, file_id in files.items():
    output_path = os.path.join("data/raw", filename)
    if os.path.exists(output_path):
        print(f"{filename} already exists. Skipping download.")
    else:
        url = f"https://drive.google.com/uc?id={file_id}"
        print(f"Downloading {filename}...")
        gdown.download(url, output_path, quiet=False)

print("\n All required files are present in data/raw/")