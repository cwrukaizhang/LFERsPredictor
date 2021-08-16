<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/cwrukaizhang/LFERsPredictor">
    <img src="templates/logo.png" alt="Logo" width="200" height="80">
  </a>

  <h3 align="center">PaDEL-DNN offline predictor</h3>

  <p align="center">
    This Github project shared some source codes from our recent research for estimating LFER descriptors for organic chemicals!
    <br />
    <a href="https://github.com/cwrukaizhang/LFERsPredictor"><strong>Explore the docs »</strong></a>
    <br />
</p>



<!-- TABLE OF CONTENTS -->



<!-- ABOUT THE PROJECT -->
## About The Project

In our recent research, we used the PaDEL package and the deep neural network to built predictive models for LFER descriptors. This project provided some codes or trained models for estimating LFER descriptorts for new chemicals and reproduce some results presented in our manuscript. For potential users, a step by step explanantion was provided in the following sections.


<!-- GETTING STARTED -->
## Getting Started

To test the built models, a python working environment including some python packages needed to be configurated first. After finishing the configuration of python environment, one can run the python script to launch the offline predicting tool in a web broswer. Then, inputing the "SMILES" of the test chemicals and the estimated LFER descriptors and the surrogate metric results will be displayed.

### Prerequisites

This is an example of how to list packages will be needed to make the build model working properly.
* Required JRE and python packages
  ```sh
  Java runtime environment
  tensorflow
  keras
  flask
  padelpy
  pubchempy
  rdkit
  ```

### Installation

1. The PaDEL package requires a Java support.
   ```sh
   Download Java SE Runtime Environment and install the software.
   ```
2. Create and activate conda virtue environment for the predicting tool
   ```sh
   conda create -n LFER_tool
   conda activate LFER_tool
   ```
3. Install required python package
   ```sh
   conda install tensorflow
   conda install keras
   conda install flask
   conda install -c rdkit rdkit
   pip install padelpy
   pip install pubchempy 
   ```
3. Clone (if git software is avaliable on the computer) or download the files of this project
   ```sh
   git clone https://github.com/cwrukaizhang/LFERsPredictor.git 
   ```
4. Swithch to the working directory and run the  app_new.py file
   ```JS
   python app_new.py
   ```
5. Input and switch the local host in a webbrowser.

<!-- CONTACT -->
## Contact



Project Link: [https://github.com/cwrukaizhang/LFERsPredictor](https://github.com/cwrukaizhang/LFERsPredictor)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [Loaders.css](https://connoratherton.com/loaders)
* [Slick Carousel](https://kenwheeler.github.io/slick)
* [Smooth Scroll](https://github.com/cferdinandi/smooth-scroll)
* [Sticky Kit](http://leafo.net/sticky-kit)
* [JVectorMap](http://jvectormap.com)
* [Font Awesome](https://fontawesome.com)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
