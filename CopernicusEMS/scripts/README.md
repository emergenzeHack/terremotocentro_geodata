## copernicus_ESMR.py :octocat: 
### Script per de-zippare ad effettuare il merge dei files downloadati da Copernicus   
  
per poter eseguire lo script e' necessario innanzitutto installare il modulo *"pyshp"*  
  
> sudo pip install pyshp  
  
Alcune linee dello script vanno modificate ed adattate alla propria situazione.  
  
>  
> ###############################################################################  
>  
> __folder_input_zip__ = "/home/geofrizz/Downloads/Copernicus/EMSR190/"  
> __folder_output_zip__ = "/home/geofrizz/Downloads/Copernicus/EMSR190/temp/"  
> __array_id__ = ["_01","_02","_03","_04","_05","_06","_07","_08","_09","_10","_11","_12","_13","_14","_15","_16","_17","_18","_19","_20","_21","_22","_23","_28","_29","_30","_31","_32"]  
> __folder_input_shp__ = folder_output_zip  
> __folder_output_shp__ = "/home/geofrizz/Downloads/Copernicus/EMSR190/EMSR190_input/"  
> __array_elements__ = ['settlements_poly_grading', 'hydrography_line_grading', 'physiography_line', 'transportation_line_grading']  
> __folder_input_merge__ = folder_output_shp  
> __folder_output_merge__ = "/home/geofrizz/Downloads/Copernicus/EMSR190/EMSR190/"  
>  
> ###############################################################################  
>  
  
**N.B.**  
* le cartelle vanno create prima di eseguire lo script;  
* nella variabile *__array_id__* vengono inseriti gli id del bbox che vengono utilizzati nel nome del file zippato;  
* nella variabile *__array_elements__* vengono inseriti gli elementi che si vogliono estrarre ed eventualmente aggiungere nel servizio wms 
  
----------------------------------------

