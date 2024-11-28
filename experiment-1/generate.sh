for bmpfile in inputs/*.bmp; do
    python3 ../prism/decode.py $bmpfile $bmpfile.wav -r 192000 -w 512
done