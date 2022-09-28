# Geospatial Pipeline Evaluation
- [**MSC**](#msc)
  - [**WMS-API**](#wms)
  - [**OGC-API**](#ogc)
  - [**Work To Do**](#work-to-do)
- [**RADARSAT1**](#radarsat1)
- [**Geospatial Work in Databricks**](#geospatial-work-in-databricks)

## **MSC**
 ECCC provides the Meteorological Service of Canada along with open data. This information can be found [**here**](https://eccc-msc.github.io/open-data/readme_en/). 
 
### **WMS**
#### **Profits based on precipitation:**

*   This was a use case was an example provided by the MSC open data portal [**here**](https://eccc-msc.github.io/open-data/usage/use-case_arthur/use-case_arthur_en/). This pipeline uses [**Web Map Services (WMS)**](https://eccc-msc.github.io/open-data/msc-geomet/web-services_en/#web-map-service-wms) and uses temporal queries to display calculated results in multiple formats. 
*   We were able to directly implement [**the script**](https://github.com/ssc-sp/geospatial-pipeline-eval/blob/main/MSC_Pipelines/MSC_precipitation_UseCase.py) into the databricks environment. To fully utlilze databricks, it is recommended that the data be placed within spark dataframes rather than pandas so that spark may run parallel jobs.

### **OGC**
#### **Retrieving and displaying hydrometric data:**

* This was a use case was an example provided by the MSC open data portal [**here**](https://eccc-msc.github.io/open-data/usage/use-case_oafeat/use-case_oafeat-script_en/5). This pipeline uses the [**GeoMet-OGC-API**](https://api.weather.gc.ca/) which leverages vector data in GeoJSON format using Open Geospatial Consortium standards. 
* [**This script**](https://github.com/ssc-sp/geospatial-pipeline-eval/blob/main/MSC_Pipelines/MSC_Hydrometric_UseCase.py) was implemented in the databricks environment however we ran into problems resolving dependencies with the mapping library cartopy. Specifically, the GEOS library. While this may be fixable in the environment the [**folium**](http://python-visualization.github.io/folium/) library to map the resulting data.
* The folium library uses the leaflet.js library and can be easily implemented using python web development tools such as flask and django (example can be found [**here**](http://python-visualization.github.io/folium/flask.html))
  *  This means that web mapping [**examples**](https://eccc-msc.github.io/open-data/usage/tutorial_web-maps_en/#tutorial-building-interactive-web-maps-with-openlayers-and-leaflet) provided by ECCC can also be implemented in databricks
*  These scripts can be better implemented within the databricks environment

#### **Testing Sparks Dataframe:**
* This script is an example of how the databricks environment can be efficiently implemented in a way that maximizes it's benefits
* We used the GeoMet API to 

### **Work To Do**
* Create a demo of a time series map using a library such as folium
* Find a way to implement cartopy for mapping of 
  * The required step here is to install [**LibGEOS**](https://libgeos.org/) onto the cluster or the notebook
  
## **RADARSAT1**
Using the Canadian Space Agencies Repo, scripts where moved in a Databricks environment to demonstrate RADARSAT-1 satetlite imagery. More details of this project can be found [**here**](https://github.com/ssc-sp/radarsat1-scripts).

## **Geospatial Work in Databricks**
* 
