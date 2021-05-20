# Lowest price notification

Here is a small but fun script i made in python. It is a script that sends an email and pops up a notification with the lowest price for a product 

The user is asked to enter a product he wants to buy from https://www.skroutz.gr/. Then a Google Chrome window is opened automatically on https://www.skroutz.gr/ , locates the Search bar using Selenium, enters the user input on search bar (send_keys) and presses enter (send_keys(Keys.RETURN)).

Once enter is pressed, it shows all the products with similar name as the user input. I locate the first element which more likely has the best match and using ActionChains which lets you take control of your mouse, i move the mouse to the element and click it. 

The next page contains all available stores that sale the current product and using Requests library i scrape all the prices and store them to a list. The list is stored in ascending order and save the lowest price product to a variable.

Next step is to use the plyer notification 



Libraries that were used: BeautifulSoup, Selenium, os, smtplib, plyer notification


