set -e

echo "Current directory:"
pwd

echo "Files before compile:"
ls -lah

g++ main.cpp -o main

echo "Files after compile:"
ls -lah