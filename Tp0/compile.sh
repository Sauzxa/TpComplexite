#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"
mkdir -p dist data

for program in Random100 Random1000 Test-1 Test-2 Test-3; do
    gcc -std=c11 -Wall -Wextra -O2 "src/${program}.c" -o "dist/${program}"
done

echo "Compilation complete. Executables are in dist/."
