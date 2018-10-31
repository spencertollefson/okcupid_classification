# Project McNulty - Online Dating: Who Wants Children?
## Spencer Tollefson
## October 31, 2018

# Project Design
OkCupid.com is an online dating platform catered toward single adults who are seeking romantic partners. Upon getting my hands on a dataset of nearly 60,000 OkCupid.com profiles, I became interested if the other attributes were indicative of people's desire to want or not want children. Interestingly enough, the dataset showed that many people chose not to provide this optional information. My assumption was this is because people do not want to be instantly filtered as a "no" if their children rearing plans do not match people who may well be good potential matches.

A model that performs well in predicting one's desire to raise children would provide better compatibility at the outset of people seeking romantic partners. Potential uses could be for individuals in a web app, 


Thus, I built models to predict if 


# Tools
* Python:
  * Data cleaning: pandas, joblib
  * Data analysis: numpy, pandas, scikit-learn, Jupyter
  * Presentation: matplotlib, seaborn
* Google Slides
* Tableau?
* Flask app? (Python tool)


# Data
The data was obtained from a (Github repo)[https://github.org/]. The original data was scraped via a Python script in June 2011. It contains profile attributes of nearly 60,000 OkCupid.com accounts which had been active during the month preceding June 15, 2011, and had San Francisco, CA as their current location.

All features may be found in the appendix. Cleaning was applied to many columns to account for grouping of multiple subjects. For example, the original data grouped religious intensity (serious, nonchalant, unserious) and the name of the religion together. By cleaning I separated these two subjects and considered them separate features.


# What I would do differently

See if certain ages are obvious (under 22, above 40) and screen out those datasets to make the modeling more predictive.

Assign ordinal values to certain features. For example, intuitively it appears there is a ranking to be derived to how much someone consumes alcohol when the optional descriptors "rarely", "socially", and "often" are used. There are numerous categorical features which I believe ordinal values could have been derived and modeled.

There was a "maybe" class for the target variable of "want offspring". With more time, I would have made a multi-class model that attempted to classify profiles as "no", "maybe", or "yes" for the target variable of wanting children.

Think more carefully about the ethical considerations involved in which features are used in the modeling. I purposely removed ethnicity and income level as I did not want my model to discriminate, but used features such as sexual orientation and religion. Considering all of this information was freely offered by users in making their profiles, perhaps there is no harm creating a model with these inputs. 
 
Considered more deeply about the real-world value of this predictive model. 
