#for bmpfile in medium/*.bmp; do
    #python3 ../prism/decode.py $bmpfile $bmpfile.wav -r 192000 -2 -s 1024
	#done

for wavfile in medium/*.wav; do
     python3 ../prism/encode.py $wavfile $wavfile.ref.bmp -2 -s 1024 -b 256
done