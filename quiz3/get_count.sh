tail -n +2 life-expectancy.csv | cut -d "," -f1 | sort | uniq -c | sort -nr 
