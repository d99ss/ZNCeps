# Project description 📜

Android APP automation using **Appium &amp; Selenium**

![](https://github.com/d99ss/ZNCeps/assets/24706768/b8497e83-69ad-42b5-8295-ad0d26ffaa7e)

The main goal of this project was to check whether the app delivery *(Zee.Now)* services a specific zip code, in this case, zip codes of the City of São Paulo. 
The idea came about when a lot of people had problems buying just because their zip codes weren't serviced, when I started to analyze I realized a lot of zip codes were within the area of delivery, but for some reason, they weren't being serviced. that's why I decided to build this script to test each zip code individually to test whether that zip code is serviced or not. 

Basically using a library called Appium and the Android Studio, I was able to install the app into a VDM to test and emulate the real process of putting each cep.
I only tested using the zip codes of the City of São Paulo, but you can test from other Brazilian cities where the delivery app operates such as Rio de Janeiro.

The full explanation is on my *[Medium post](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white
)*.

## Library 📚 

- Appium
- Selenium 
- Pandas

Just running the requirements.txt file you can install all the required libraries/dependencies via **__pip install_**. 
Apart from the required libraries, there are two ways to emulate the app:
   1-  If you have the App's *__APK__* you **must have the __Android Studio_** to install the APP in a Virtual Device Manager (VDM).
   2- You can test the app using a real device.

  Both ways work with pros and cons. It's up to you to decide what works best.

## Resources ☕ 
The following resources can be useful if you don't have familiarity with Automation.
I highly recommend reading the first resource, since the setup just to make the app run is highly complicated, tricky, and cumbersome it takes a lot of time to get it up and running.

 - [Appium GitHub guide](https://github.com/clarabez/appium)
 - [Appium Website](https://appium.io/docs/en/2.1/)
 - [Android Studio](https://developer.android.com/studio?gclid=Cj0KCQjwi7GnBhDXARIsAFLvH4m_mNywnlThdLkd5YLBdBH_UtAF7_0WE_iXmyNCnqwByrqWKjTF9BMaApc0EALw_wcB&gclsrc=aw.ds)
 -  [Appium Testing with Real Devices](https://github.com/clarabez/appium)
