import json

# Load the JSON file
with open("buckets.json", "r") as file:
    data = json.load(file)

# Extract bucket list
buckets = data["buckets"]

# Print bucket summary
print("\n📌 Bucket Summary:")
for bucket in buckets:
    print(
        f"Name: {bucket['name']}, Region: {bucket['region']}, Size: {bucket['sizeGB']} GB, Versioning: {bucket['versioning']}"
    )

# Modify a specific bucket (example: updating prod-data size and disabling versioning)
for bucket in buckets:
    if bucket["name"] == "prod-data":
        bucket["sizeGB"] = 150
        bucket["versioning"] = False
        print(f"\n✅ Updated {bucket['name']} bucket:", bucket)

# Save the changes back to the file
with open("buckets.json", "w") as file:
    json.dump(data, file, indent=2)

print("\n🎯 Changes saved successfully!")
