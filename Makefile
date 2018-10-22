convert:
	./dbc2dbf.sh
	mkdir -p data/csv
	python dbf2csv.py