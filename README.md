# Lowest price notification

Here is a small but fun script i made in python. It is a script that sends an email and pops up a notification with the lowest price for a product from https://www.skroutz.gr/. Some of the libraries that were used are: BeautifulSoup, Selenium, os, smtplib, plyer notification

## Analyzing the steps

### Searching for the product

The user inputs a product he wants to buy from https://www.skroutz.gr/. Selenium opens a Google Chrome window on Skroutz.gr , locates the search bar, where it enters the user input (using send_keys) and presses enter ***(send_keys(Keys.RETURN))***. 

### Gathering the data

Once enter is pressed, the next page shows all available products with similar name as the user input. I locate the first element (which more likely has the best match) and using **ActionChains** (which lets you take control of your mouse), i move the mouse to the element and click it. 

The next page contains all available stores that sale the current product. Using **BeautifulSoup** i scrape all the prices and store them to a list. The list is sorted in ascending order and the lowest price is saved to a variable. 

### User notification

The user is informed about the lowest price with two ways. 
1) Using plyer notification in which i specified the title and the message of the notification.
2) Using the Smtplib library to send an email. We must first connect to the port ***with smtplib.SMTP("smtp.gmail.com", 587) as smtp:***. Then identify ourselves to the server with the ***smtp.ehlo()***. Final step is to login using our email and password and specify the subject and message we want to send.                                         
![image](https://user-images.githubusercontent.com/72921465/119180555-1b7e4000-ba79-11eb-83cd-245ac148f0e0.png)


A good practice when you have to upload in public a script that will use your email and password is to save them as environmental variables in your computer. So whenever you want to call them you can use the Os library as shown below.                                                                         
![image](https://user-images.githubusercontent.com/72921465/119179139-3e0f5980-ba77-11eb-8b5c-0b8d32bf04b6.png)








