mkdir -p output && for file in regions/*.txt; do 
    region=$(basename "$file" .txt)

    grep -f "$file" data/life-expectancy.csv | grep 1990 > output/${region}_life_1990.csv
    grep -f "$file" data/gdp-per-capita-maddison-project-database.csv | grep 1990 > output/${region}_gdp_1990.csv
    grep -f "$file" data/trade-as-share-of-gdp.csv | grep 1990 > output/${region}_trade_1990.csv
done