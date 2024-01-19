cd ../MCB185/data
gunzip -c dictionary.gz | grep "^[zoniacr]*r[zoniacr]*$" | grep -v -E "^[zoniacr].{0,1}[zoniacr]$"