# Faultlines 
by Shawn Sobieski

## Goal
As American political opinion seems to get more and more bifricated, I intend to analyze this trend using machine learning techniques to predict political opinions. By assessing the differences in party opinion we can see what each party stands for and how people look at that   

The goal of this project is to get a better understanding of what the two parties in America stand for. What do they believe, and where are they headed in their beliefs?

## Methodology
I will plot trends in political opinion to get an understanding of how Americans feel about particular issues. Using time series analysis I will attempt to predict where these trends are heading. I will repeat this analysis for several questions, and break the data down into political groupings such as voters and non-voters, or Republicans, Democrats and Independents. 

## The Data
Data for this analysis was collected from the General Social Survey conducted by the University of Chicago. It spans 50 years and over 30 questions.  

## The Model
The model used for this analysis was an ARIMA model. I used a function to iterate through and optimize parameters and make predictions.  

## Conclusion
The data showed that there is clear increase among Independent affiliated voters. As a result the opinions that characterize each party are growing farther and farther apart. Interestingly, in many cases opinions overall did not change much despite the fact that party differences have grown apart in almost every case.  


<div class='tableauPlaceholder' id='viz1596132431301' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pa&#47;PartyAffiliation_15955565122690&#47;Story1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='PartyAffiliation_15955565122690&#47;Story1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pa&#47;PartyAffiliation_15955565122690&#47;Story1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1596132431301');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='550px';vizElement.style.height='597px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
