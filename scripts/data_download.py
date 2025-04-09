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


# Download each file
for filename, file_id in files.items():
    url = f"https://drive.google.com/uc?id={file_id}"
    output_path = os.path.join("data/raw", filename)
    print(f"Downloading {filename}...")
    gdown.download(url, output_path, quiet=False)

print("All files downloaded to data/raw/")
