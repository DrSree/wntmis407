import pandas as pd

print "Downloading file...\n"

url = 'https://health.data.ny.gov/api/views/jxy9-yhdk/rows.csv?accessType=DOWNLOAD'
baby_names = pd.read_csv(url)

print "##########"
print "Popular Baby Names"
print "##########"
male_names = baby_names.query('Sex == "M" and Count >= 225')
data_str = str(male_names)
lines = data_str.split("\\n")
file = open("MaleBabies.csv", "w")

for line in lines:
    file.write(line + "\n")
    file.close()

read_file = pd.read_csv("MaleBabies.csv")
print read_file

