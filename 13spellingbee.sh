cd ../MCB185/data
gunzip -c dictionary.gz | grep "^[zoniacr]*r[zoniacr]*$" | grep -v -E "^.{0,3}$"
