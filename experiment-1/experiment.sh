for wavfile in inputs/*.wav; do
    python3 apply.py $wavfile "response/$(basename $wavfile)"
done

for wavfile in response/*.wav; do
    python3 ../prism/encode.py $wavfile response/$(basename $wavfile .wav).bmp -b 256
done