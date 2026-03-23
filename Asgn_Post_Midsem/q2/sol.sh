mkdir -p output && for file in regions/*.txt; do 
    region=$(basename "$file" .txt)
    grep -f "$file" data/life-expectancy.csv | grep 2020 > output/${region}_life_2020.csv
done