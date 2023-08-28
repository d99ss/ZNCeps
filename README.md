# Project description 📜
Android APP automation using **Appium &amp; Selenium**.
The main goal of this project was to check whether the app delivery *(Zee.Now)* services a specific zip code, in this case, zip codes of the City of São Paulo. 
The idea came about when a lot of people had problems buying just because their zip codes weren't serviced, when I started to analyze I realized a lot of zip codes were within the area of delivery, but for some reason, they weren't being serviced. I came to the conclusion that zipcodes like the ones below aren't serviced because in the *Correios* database they're listed with other names, Even though the neighborhood is Rio Pequeno and are clearly serviced the ceps below aren't just because they're listed with different names.

  -![image](https://github.com/d99ss/ZNCeps/assets/24706768/254c52e2-761d-4d3c-b52e-8cb4a73ddb07)

The full explanation is on my *[Medium post](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white
)*.
Basically using a library called Appium and the Android Studio, I was able to install the app into a VDM to test and emulate the real process of putting each cep individually to test whether that zip code is serviced or not. 

## Library ☕️

- Appium
- Selenium
- Pandas

Just running the requirements.txt file you can install all the required libraries/dependencies. 
Apart from the required libraries, you **must have the Android Studio** to emulate the app in a Virtual Device to test the app. 

## Resources 
The following resources can be useful if you don't have familiarity with Automation
 - [Appium GitHub guide](https://github.com/clarabez/appium)
 - [Appium Website](https://appium.io/docs/en/2.1/)
 - [Android Studio](https://developer.android.com/studio?gclid=Cj0KCQjwi7GnBhDXARIsAFLvH4m_mNywnlThdLkd5YLBdBH_UtAF7_0WE_iXmyNCnqwByrqWKjTF9BMaApc0EALw_wcB&gclsrc=aw.ds) 
