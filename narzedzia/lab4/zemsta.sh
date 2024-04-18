wget "https://wolnelektury.pl/media/book/txt/zemsta.txt"
grep -n AKT zemsta.txt

line_numbers=(39 1563 3337 4896 6546)
for i in 0 1 2 3
do
    start=${line_numbers[$i]}
    end=${line_numbers[$(($i+1))]}
    head -n $(($end - 1)) zemsta.txt | tail -n $(($end - $start + 1)) > "akt"$(($i+1))
done

for file in akt1 akt2 akt3 akt4
do
    grep -c SCENA $file
done

grep -c -i "mocium panie" zemsta.txt
