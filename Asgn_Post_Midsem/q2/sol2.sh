mkdir -p output && for file in regions/*.txt; do 
    region=$(basename "$file" .txt)

    grep -f "$file" data/life-expectancy.csv | grep 2020 > output/${region}_life_2020.csv
    grep -f "$file" data/gdp-per-capita-maddison-project-database.csv | grep 2020 > output/${region}_gdp_2020.csv
    grep -f "$file" data/co-emissions-per-capita.csv | grep 2020 > output/${region}_co2_2020.csv
    grep -f "$file" data/trade-as-share-of-gdp.csv | grep 2020 > output/${region}_trade_2020.csv

done