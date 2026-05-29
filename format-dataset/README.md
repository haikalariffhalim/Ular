 ## multi-line string assignment
 
 Python code that starts a **multi-line string assignment**:

- `sql_output` — a variable name
- `=` — assignment operator
- `"""` — the start of a triple-quoted string

Triple quotes (`"""` or `'''`) in Python create multi-line strings that can span across multiple lines while preserving newlines and indentation. The string continues until it encounters the closing `"""`.

**Example:**

```py
sql_output = """
SELECT * FROM users
WHERE id = 1
AND status = 'active'
"""
```

In this case, `sql_output` would contain a multi-line SQL query as a string.


Triple-quoted strings are also commonly used for **docstrings** (documentation strings in functions, classes, and modules), but when assigned to a variable like `sql_output = """`, it's just creating a regular multi-line string value.
