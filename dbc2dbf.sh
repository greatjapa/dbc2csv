for file in data/*.dbc; do
  ./blast-dbf/blast-dbf "$file" "${file%%.*}.dbf"
  echo "$file converted to dbf"
done