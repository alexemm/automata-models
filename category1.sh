echo "We start with an implementation from category 1 (egrep) -----"
for file in regex_tests/*; do
  echo $file
  START=$(date +%s.%N)
  echo "Output:"
  egrep -f regex.txt $file
  END=$(date +%s.%N)
  DIFF=$(echo "$END - $START" | bc)
  echo 'It took'
  echo $DIFF
  echo "seconds"
  echo ""
done

echo "Category 1 done -----"