convert:
	./dbc2dbf.sh
	mkdir -p data/csv
	python3 dbf2csv.py