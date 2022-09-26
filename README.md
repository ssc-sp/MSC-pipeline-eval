# Geospatial Pipeline Evaluation
- [**MSC**](#msc)
  - [**Pipelines**](#pipelines)
  - [**Work to do**](#todo)
- [**RADARSAT1**](#radarsat1)

## **MSC**
 ECCC provides the Meteorological Service of Canada along with open data. This information can be found [**here**](https://eccc-msc.github.io/open-data/readme_en/). 
 
### **Pipelines**
Profits based on precipitation:

*   This was a use case was an example provided by the MSC open data portal [**here**](https://eccc-msc.github.io/open-data/usage/use-case_arthur/use-case_arthur_en/). This pipeline uses [**Web Map Services (WMS)**](https://eccc-msc.github.io/open-data/msc-geomet/web-services_en/#web-map-service-wms) and uses temporal queries to display calculated results in multiple formats. We were able to directly implement the script into the databricks environment. To fully utlilze databricks, it is recommended that the data be placed within spark dataframes rather than pandas so that spark may run parallel jobs.

Retrieving and displaying hydrometric data:

* This was a use case was an example provided by the MSC open data portal [**here**](https://eccc-msc.github.io/open-data/usage/use-case_oafeat/use-case_oafeat-script_en/5). This pipeline uses the [**GeoMet-OGC-API**](https://api.weather.gc.ca/) which leverages vector data in GeoJSON format using Open Geospatial Consortium standards. This script was implemented in the databricks environment however we ran into problems resolving dependencies with the mapping library cartopy. Specifically, the GEOS library. While this may be fixable in the environment the folium library to map the resulting data.

### **todo**


## **RADARSAT1**
Using the Canadian Space Agencies Repo, scripts where moved in a Databricks environment to demonstrate RADARSAT-1 satetlite imagery. More details of this project can be found [**here**](https://github.com/ssc-sp/radarsat1-scripts).
