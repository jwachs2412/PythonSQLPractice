import csv

def process_csv():
    with open("data.csv", "r") as file:
        reader = csv.DictReader(file)
        entries = list(reader)
        print(f"Total entries: {len(entries)}")
        
        print("People over 30:")
        filtered = [entry for entry in entries if int(entry["Age"]) > 30]
        for person in filtered:
            print(person)
            
    with open("filtered_data.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Age", "City"])
        writer.writeheader()
        writer.writerows(filtered)
    print("Filtered data saved to 'filtered_data.csv'.")
    
process_csv()