import csv

# Open the .dat file and read the content
with open('winding.dat\winding.dat', 'r') as dat_file:
    data = dat_file.readlines()

# Open a new CSV file to write the content
with open('processData.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    
    # Write the header row with the column titles
    writer.writerow(['u1', 'u2', 'u3','u4', 'u5', 'y1', 'y2'])
    
    # Write the data rows
    for line in data:
        # Assuming the data in the .dat file is space-separated
        row = line.strip().split()  # Customize the split method based on your data
        writer.writerow(row)