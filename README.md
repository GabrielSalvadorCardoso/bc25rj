# bc25rj
bc25rj uses python3 and pip

## intall project python dependencies
pip install -r requirements.txt

## bc25rj uses mapnik, to install it
https://github.com/mapnik/mapnik/wiki/UbuntuInstallation

## in the case of errors involving the C++ compiler
https://github.com/mapnik/mapnik/issues/3769

## install mapnik python bidings
pip3 install mapnik

## if the previous command doesn't work
https://github.com/mapnik/python-mapnik

bc25rj uses PostgreSQL with spatial extansion PostGIS. Feel free to use whatever database with spatial extansion you want

## bc25rj spatial data
ftp://geoftp.ibge.gov.br/cartas_e_mapas/bases_cartograficas_continuas/bc25/rj/versao2018/shapefiles/

## using shp2pgsql to transfer shapefiles to postgres/postgis
https://www.bostongis.com/pgsql2shp_shp2pgsql_quickguide.bqg
