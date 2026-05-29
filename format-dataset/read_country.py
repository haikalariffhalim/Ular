
# Read the country.sql file
with open('dataset/country.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Extract data rows (skip header and separator lines)
data_rows = []
for line in lines:
    # Skip separator and header lines
    if line.startswith('+') or 'Code' in line:
        continue
    # Only process lines that start with |
    if line.startswith('|'):
        # Split by | and clean
        parts = [p.strip() for p in line.split('|')]
        # Remove empty first and last elements (from | at start/end)
        parts = parts[1:-1]
        if len(parts) == 14:
            data_rows.append(parts)

print(f"Found {len(data_rows)} country records")
print("\nFirst 3 records:")
for i, row in enumerate(data_rows[:3]):
    print(f"\nRecord {i+1}:")
    columns = ['Code', 'Name', 'Continent', 'Region', 'SurfaceArea', 'IndepYear', 'Population', 'LifeExpectancy', 'GNP', 'GNPOld', 'LocalName', 'GovernmentForm', 'Capital', 'Code2']
    for col, val in zip(columns, row):
        print(f"  {col}: {val}")
