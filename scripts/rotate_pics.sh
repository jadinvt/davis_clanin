export y=$1
shift
for x in $@ ; do
    convert img_${x}_large.jpg -rotate $y  img_${x}_large.jpg; 
    convert img_${x}_medium.jpg -rotate $y  img_${x}_medium.jpg; 
    convert img_${x}_small.jpg -rotate $y  img_${x}_small.jpg; 
done
