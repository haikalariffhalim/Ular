
# Read the country.sql file
with open('dataset/country.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Extract data rows
data_rows = []
for line in lines:
    if line.startswith('+') or 'Code' in line:
        continue
    if line.startswith('|'):
        parts = [p.strip() for p in line.split('|')]
        parts = parts[1:-1]
        if len(parts) == 14:
            data_rows.append(parts)

print(f"Parsed {len(data_rows)} country records")


# Generate SQL
sql_output = """
-- Country Table
-- Stores information about countries worldwide

CREATE TABLE IF NOT EXISTS country (
    Code CHAR(3) PRIMARY KEY,
    Name VARCHAR(52) NOT NULL UNIQUE,
    Continent VARCHAR(50) NOT NULL,
    Region VARCHAR(26) NOT NULL,
    SurfaceArea DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    IndepYear SMALLINT,
    Population INT NOT NULL DEFAULT 0,
    LifeExpectancy DECIMAL(3, 1),
    GNP DECIMAL(10, 2),
    GNPOld DECIMAL(10, 2),
    LocalName VARCHAR(45) NOT NULL,
    GovernmentForm VARCHAR(45) NOT NULL,
    Capital INT,
    Code2 CHAR(2),
    INDEX idx_continent (Continent),
    INDEX idx_region (Region),
    INDEX idx_population (Population)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Country Data
"""

# Build INSERT statements
batch_size = 50
for batch_start in range(0, len(data_rows), batch_size):
    batch_end = min(batch_start + batch_size, len(data_rows))
    batch = data_rows[batch_start:batch_end]

    insert_values = []
    for row in batch:
        code, name, continent, region, surface_area, indep_year, population, life_exp, gnp, gnp_old, local_name, govt_form, capital, code2 = row

        # Escape single quotes
        name_esc = name.replace("'", "''")
        continent_esc = continent.replace("'", "''")
        region_esc = region.replace("'", "''")
        local_name_esc = local_name.replace("'", "''")
        govt_form_esc = govt_form.replace("'", "''")

        # Handle NULL values
        indep_year_val = 'NULL' if indep_year == 'NULL' else indep_year
        life_exp_val = 'NULL' if life_exp == 'NULL' else life_exp
        gnp_val = 'NULL' if gnp == 'NULL' else gnp
        gnp_old_val = 'NULL' if gnp_old == 'NULL' else gnp_old
        capital_val = 'NULL' if capital == 'NULL' else capital
        code2_val = code2 if code2 != 'NULL' else 'NULL'

        # Build the VALUES tuple
        if code2_val == 'NULL':
            value_tuple = f"('{code}', '{name_esc}', '{continent_esc}', '{region_esc}', {surface_area}, {indep_year_val}, {population}, {life_exp_val}, {gnp_val}, {gnp_old_val}, '{local_name_esc}', '{govt_form_esc}', {capital_val}, NULL)"
        else:
            value_tuple = f"('{code}', '{name_esc}', '{continent_esc}', '{region_esc}', {surface_area}, {indep_year_val}, {population}, {life_exp_val}, {gnp_val}, {gnp_old_val}, '{local_name_esc}', '{govt_form_esc}', {capital_val}, '{code2_val}')"

        insert_values.append(value_tuple)

    sql_output += "INSERT INTO country (Code, Name, Continent, Region, SurfaceArea, IndepYear, Population, LifeExpectancy, GNP, GNPOld, LocalName, GovernmentForm, Capital, Code2) VALUES\n"
    sql_output += ",\n".join(insert_values)
    sql_output += ";\n\n"

# Write the output
with open('dataset/country.sql', 'w', encoding='utf-8') as f:
    f.write(sql_output)

print(f"Generated formatted SQL file")
print(f"File size: {len(sql_output) / 1024:.1f} KB")
