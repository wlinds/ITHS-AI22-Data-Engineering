files=("note1.txt" "note2.txt" "note3.txt" "note4")

for filename in "${files[@]}"; do
    touch "$filename"
done