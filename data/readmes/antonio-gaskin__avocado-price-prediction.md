# Avocado Price Prediction using FbProphet

- Data represents weekly 2018 retail scan data for National retail volume (units) and price. 
- Retail scan data comes directly from retailers’ cash registers based on actual retail sales of Hass avocados. 
- The Average Price (of avocados) in the table reflects a per unit (per avocado) cost, even when multiple units (avocados) are sold in bags. 
- The Product Lookup codes (PLU’s) in the table are only for Hass avocados. Other varieties of avocados (e.g. greenskins) are not included in this table.

Some relevant columns in the dataset:

- Date - The date of the observation
- AveragePrice - the average price of a single avocado
- type - conventional or organic
- year - the year
- Region - the city or region of the observation
- Total Volume - Total number of avocados sold
- 4046 - Total number of avocados with PLU 4046 sold
- 4225 - Total number of avocados with PLU 4225 sold
- 4770 - Total number of avocados with PLU 4770 sold

## Data Visualization

![image](https://user-images.githubusercontent.com/50113394/126956154-705a2cd9-fccb-4848-9ed7-2fa3538c10f1.png)  
Avocado Sales from 2015 to 2018.  

![image](https://user-images.githubusercontent.com/50113394/126956276-7d1fe396-4c2e-40b0-beb8-4314cd81230f.png)  
Avocado average price per unit, from 2015 to 2018.  

## FbProphet

![image](https://user-images.githubusercontent.com/50113394/126956451-eaba4097-7250-4a9a-887a-89affff5d07c.png)  
Average Unit Price forecast for the year 2019.  

![image](https://user-images.githubusercontent.com/50113394/126956586-e0df2fab-8321-4988-bf2d-f7b1530b7f2e.png)  
Average Unit Price trend yearly.  

![image](https://user-images.githubusercontent.com/50113394/126956620-7fd9e7d0-6fed-4f9f-ad09-1d852dd76866.png)  
Average Unit Price trend monthly.  

