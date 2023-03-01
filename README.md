# foundationshades


## Purpose of this project: 
As an avid makeup consumer, I realized much of the brands I was purchasing from did not carry colors that catered towards women of color. This project hopes to shed light on the lack of foundation shades for ethnic/people of color, especially from large makeup conglomerates. 

## Description: 
From Kaggle, I contributed and manipulated a public database of makeup (foundation) products, with their corresponding product names, brand names, hex codes (color codes), HSV values, and lightness values. Much of the color matching from swatches of makeup were appointed through CIELAB color lab to find and attribute these values to their corresponding products. With added products and changing product lines, updates to this project is much needed. I started this back in September 2022 and just now uploaded to Git and public Tableau.

### About HSV and L values:

HSV stands for Hue - Saturation - Value. 

**Hue** is represented with an angle (0 to 360 degrees), with the following correspondants: 

- 0-60	Red
- 60-120	Yellow
- 120-180	Green
- 180-240	Cyan
- 240-300	Blue
- 300-360	Magenta


**Saturation** indicates how much 'gray' is in the space. When 0, the color is gray and when 1.0 the color is a primary color. 

**Value** records the brightness of color. When 0, the color is black, when 1.0, the color is white (Scale is 0-100 or 0 - 1.0).

**Lightness** (L) is also on a scale of 0 being black, and 100% being white. 

## How Values are Captured: 
CIELAB was used to color grab a foundation shade/color through an image, giving its resulting hex code (web color), HSV, and HSL values. 
There is a slight distinct difference between color in person and a color shown on a screen for example, but not to an extent for it to be a noticeable and great effect on the results since we pay more importance on extreme values. 


## Data Analysis: 
I created a dashboard using Tableau that can aid consumers in deciding which brands  have best range of shades, especially those that cater specifically towards women of color. I also paired this project with a paper for my marketing class, in which I did a consumer and product analysis for ItCosmetics (a brand notorious for providing low shade ranges).  
