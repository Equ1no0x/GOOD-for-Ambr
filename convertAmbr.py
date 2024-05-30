import json

# Replace the file name with the resulting file exported from your desired program in GOOD JSON format.
# Recommendation: Inventory_Kamera
data_file = 'YOUR_FILE_NAME_HERE.json'

try:
    with open(data_file, 'r', encoding='utf-8') as f3:
        file3_data = json.load(f3)
except FileNotFoundError:
    print(f"The file '{data_file}' is not available.")
    input("Press any key to exit...")
    exit()

# Loads the template containing all IDs from Ambr materials list
with open('ambrTemplate.json', 'r', encoding='utf-8') as f1:
    file1_data = json.load(f1)

# Load the IDs corresponding to each material ID in Ambrs list
with open('IDs.json', 'r', encoding='utf-8') as f2:
    file2_data = json.load(f2)

# Move the values over from the exported file
materials_data = file3_data.get("materials", {})

# Remove unwanted characters in IDs, just in case
file2_data_cleaned = {k: v.replace("—", "") if isinstance(v, str) else v for k, v in file2_data.items()}
file2_data_cleaned = {k: v.replace("'", "") if isinstance(v, str) else v for k, v in file2_data.items()}

# Some IDs are not available on the exported files, like Ores
# This section can be changed to support feature items that are also not exported, if needed
requested_keys = {
    "104011": "Enhancement Ore Count",
    "104012": "Fine Enhancement Ore Count",
    "104013": "Mystic Enhancement Ore Count"
}

# Prompt the user to input values for the requested keys
for key, description in requested_keys.items():
    value = input(f"Please enter the value for '{description}' ({key}): ")
    file1_data[0]['material'][key] = int(value)  # Convert input value to int

# Update the "material" field in ambrTemplate for other keys
for item in file1_data:
    if 'material' in item:
        for key in item['material']:
            if key not in requested_keys:
                material_name = str(file2_data_cleaned.get(key, ""))  # Ensure material_name is a string
                for material_key in materials_data.keys():
                    if material_name.lower() == material_key.lower():
                        item['material'][key] = materials_data[material_key]
                        break  # Stop searching once a match is found

# Save the updated data to a new JSON file
with open('updated_ambrTemplate.json', 'w', encoding='utf-8') as outfile:
    json.dump(file1_data, outfile, indent=4)

print("Updated file saved as updated_ambrTemplate.json")
input("Press any key to exit...")
