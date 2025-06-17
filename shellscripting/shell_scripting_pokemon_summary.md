
# 🧠 Shell Scripting Summary: Pokémon API Project

This document summarizes key concepts, commands, and functions used in automating and processing Pokémon API data using shell scripting.

---

## 🗂️ Topics Covered

1. [Variables and Arguments](#variables-and-arguments)
2. [Functions in Bash](#functions-in-bash)
3. [API Requests using curl](#api-requests-using-curl)
4. [JSON Parsing with jq](#json-parsing-with-jq)
5. [Text Processing with awk and sed](#text-processing-with-awk-and-sed)
6. [Loops and Arrays](#loops-and-arrays)
7. [Error Handling and Retry Logic](#error-handling-and-retry-logic)
8. [Parallel Processing with Background Jobs](#parallel-processing-with-background-jobs)
9. [Job Control: jobs and kill](#job-control-jobs-and-kill)

---

## 📌 Variables and Arguments

- `name="$1"`: Assigns the first argument passed to a function/script to the variable `name`.

---

## 🧩 Functions in Bash

```bash
my_function() {
    name="$1"
    echo "Hello, $name!"
}

my_function "Pikachu"  # Output: Hello, Pikachu!
```

- Functions promote code reuse and readability.
- Positional arguments like `$1`, `$2`, etc., pass input into functions.

---

## 🌐 API Requests using `curl`

```bash
curl -s -f "https://pokeapi.co/api/v2/pokemon/pikachu" -o pikachu.json
```

- `-s`: Silent mode.
- `-f`: Fail silently on HTTP errors.
- `-o`: Output file.

---

## 🧬 JSON Parsing with `jq`

```bash
jq -r '.types[0].type.name' pikachu.json
```

- Extracts nested JSON data.
- `-r`: Raw output (without quotes).
- `.types[0].type.name`: Navigates JSON structure.

---

## ✂️ Text Processing with `awk` and `sed`

### `awk`

- Used for column-based operations and reporting.

```bash
awk -F',' 'NR>1 { height+=$2; weight+=$3 } END { print height, weight }'
```

### `sed`

- Stream editor, used for inline editing.

```bash
echo "pikachu" | sed 's/.*/\\u&/'  # Output: Pikachu
```

---

## 🔁 Loops and Arrays

```bash
POKEMONS=(bulbasaur ivysaur)
for name in "${POKEMONS[@]}"; do
  echo "$name"
done
```

- `"${POKEMONS[@]}"`: Expands all elements.
- `for ... in`: Loops through each item.

---

## ❗ Error Handling and Retry Logic

```bash
max_retries=3
attempt=1
while [ $attempt -le $max_retries ]; do
  curl ... && break || attempt=$((attempt+1))
done
```

- Repeats request up to 3 times on failure.
- Logs errors with timestamps to `errors.txt`.

---

## ⚡ Parallel Processing with Background Jobs

```bash
fetch_pokemon "$name" &
```

- `&`: Run in background.
- `wait`: Wait for all background jobs to complete.

---

## 🔧 Job Control: `jobs` and `kill`

```bash
jobs        # Lists all background jobs
kill %1     # Kills job with ID 1
fg %1       # Brings job to foreground
```

Used to manage concurrent jobs in shell sessions.

---

## 📄 Sample Function with Job Control

```bash
fetch_pokemon() {
    name="$1"
    curl -s -f "https://pokeapi.co/api/v2/pokemon/$name" -o "$name.json"
}

for name in "${POKEMONS[@]}"; do
    fetch_pokemon "$name" &
done

jobs
wait
```

---

## ✅ Final Notes

- Shell scripting is powerful for automation.
- Use `jq`, `awk`, and `sed` to parse and process data.
- Manage concurrency with background jobs, `wait`, `jobs`, and `kill`.

---

**Happy scripting! 🐚✨**
