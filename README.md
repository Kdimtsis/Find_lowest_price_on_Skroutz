# Lowest price notification

Here is a small but fun script i made in python. It is a script that sends an email and pops up a notification with the lowest price for a product from https://www.skroutz.gr/. Some of the libraries that were used are: BeautifulSoup, Selenium, os, smtplib, plyer notification

## Analyzing the steps

1) The user inputs a product he wants to buy from https://www.skroutz.gr/. Then a Google Chrome window is opened automatically on Skroutz , locates the search bar using Selenium, where it enters the user input (using send_keys) and presses enter (send_keys(Keys.RETURN)). 

2) Once enter is pressed, the next page shows all available products with similar name as the user input. It locates the first element (which more likely has the best match) and using ActionChains (which lets you take control of your mouse), it moves the mouse to the element and clicks it. 

3) The next page contains all available stores that sale the current product. Using BeautifulSoup i scrape all the prices and store them to a list. The list is sorted in ascending order and the lowest price is saved to a variable. 

4) Final step is to inform the user about the lowest price with a pop-up notification and an email. To pop-up a notification i used the plyer notification in which i specified the title and the message of the notification. To send an email i used the Smtplib library. 







