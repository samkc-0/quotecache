# quotecache

## example usage:

```
pip install wikiquote
chmod +x main.py
./main.py 'Victor Hugo' --lang fr
cp .quotecache ~/.quotecache
```

then, in your `.bashrc`:

echo `awk 'BEGIN {srand()} {lines[NR]=$0} END {print lines[int(rand()*NR)+1]}' .quotecache` "(Victor Hugo)"


