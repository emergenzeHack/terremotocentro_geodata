# Dati vettoriali aggregati da Copernicus EMSR190: Earthquake in Central Italy

-----

I dati sono aggiornati al 3 Novembre 2016

-----

Questa cartella contiene dati vettoriali aggregati a partire dal servizio Copernicus Emergency Management Service.

In particolare i dati sono relativi all'attivazione _"EMSR190: Earthquake in Central Italy"_ ().

Nella cartella *vector_data* è attualmente contenuto un solo layer vettoriale in formato shapefile (*settlements_poly_grading_merged.shp*) che rappresenta la classificazione (così come effettuata da Copernicus EMS) dei danni subiti dagli edifici in seguito al terremoto di Ottobre 2016 in centro Italia.

La valutazione è stata effettuata secondo le seguenti classi:

![Legenda settlements_poly_grading](./vector_data/settlements_poly_grading_legend.png)

Il layer *settlements_poly_grading_merged.shp* è stato aggregato (operazione *merge* effettuata in ambiente QGIS 2.16) a partire dai layers contenuti nel file [*shapefileList.txt*](./vector_data/shapefile.txt), tutti scaricati dalla pagina http://emergency.copernicus.eu/EMSR190.

All'interno della stessa cartella sono anche contenuti dei file di stile utilizzabili in QGIS (*settlements_poly_grading.qml*) e in servizi WMS (*settlements_poly_grading.sld*).

La cartella [*old*](./vector_data/old/) contiene invece vecchie versioni non più aggiornate del file conservate come riferimento.

## Servizio WMS

Per poter utilizzare il layer come riferimento per il riutilizzo delle informazioni di valutazione dei danni, è stato anche predisposto un servizio WMS:
http://cigno.ve.ismar.cnr.it:80/geoserver/geonode/settlements_poly_grading_merged/ows?service=wms&version=1.3.0&request=GetCapabilities

## Data policy Copernicus EMS

I dati originali sono pubblicati da Copernicus EMS e quindi per utilizzo e citazioni si deve fare riferimento alle informazioni contenute nel sito, in particolare :

Under Copernicus and Commission Delegated Regulations [Regulation (EU) No 377/2014 and commission Delegated Regulation (EU) No 1159/2013] the information produced by the Copernicus Emergency Management Service shall be made available to the public on a full, open and free-of-charge basis. However, under exceptional circumstances, dissemination restrictions may be imposed for security reasons or for the protection of third party rights. See also detailed Copernicus EMS Data and Dissemination Policy. For more information: http://emergency.copernicus.eu/mapping/ems/cite-copernicus-ems-mapping-portal

The resource has to be cited as follows: "Copernicus Emergency Management Service (© 2016 European Union), EMSR190 Earthquake in Central Italy (http://emergency.copernicus.eu/EMSR190)"
