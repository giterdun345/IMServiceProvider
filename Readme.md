<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** giterdun345, imServiceProvider, twitter_handle, jketterer@illustrativemathematics.org, imServiceProvider, project_description
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->-

[![GNU License][license-shield]](./LICENSE)
[![LinkedIn][linkedin-shield]][linkedin-url]
<!-- [![Heroku Status][heroku-shield]][heroku-url] -->


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/giterdun345/imServiceProvider">
    <img src="logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">IM Service Provider</h3>
  <img src="https://heroku-status-badges.herokuapp.com/immense-plains-50482" alt="server status">

  <p align="center">
    This is a service provider, or a middleman, between Wrike and any third party application.
    This project currently utilizes Wrike API and Google API's for generating a living document for Priorities. The document is based on data submitted from a request/issue form in Wrike. A template is copied and filled with the data from the request/issue form. Users can update Wrike with data that has been input into the document. Also, project status can 
    be changed in the document which is then updated into Wrike. 
    <br />
    <!-- <a href="https://github.com/giterdun345/imServiceProvider"><strong>Explore the docs »</strong></a> -->
    <br />
    <!-- <a href="https://github.com/giterdun345/imServiceProvider">View Demo</a> -->
    .
    <a href="https://github.com/giterdun345/imServiceProvider/issues">Report Bug</a>
    ·
    <a href="https://github.com/giterdun345/imServiceProvider/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
The project was created for IM to increase efficiency, ease use in Wrike and to make people's lives a little easier.
There are many issues with Wrike Integrate and Workato and to resolve these issues, a custom service provider was created
that is scalable, fast, and secure. This project has eliminated the 100 API calls quota, and 30 minute wait time in Workato/Wrike Integrate. Now, IM has greater limits of 500 requests per 100 seconds per project, and 100 requests per 100 seconds per user. There is no wait time reducing the 30 minute wait time to milliseconds. Furthermore, there is also a 100 job limit in Workato; in other words, IM would only be allowed to make 100 API calls based on a trigger for the whole month. This project eliminates any monthly quota.

### Built With

* Django
* Django Rest Framework
* Google Drive API
* Google Sheets API
* Wrike API

<!-- GETTING STARTED -->
## Getting Started

Getting started requires the current service account to be authorized. Please follow the link below to learn more about authorizing this application's service account for a domain wide authority.
<br/>
<a href="https://developers.google.com/identity/protocols/oauth2/service-account/#delegatingauthority">Domain Authority<a>
<br/>

### Installation
<a href="https://developers.google.com/apps-script/add-ons/how-tos/publish-add-on-overview">Read the Docs</a>


<!-- USAGE EXAMPLES -->
## Usage



<!-- ROADMAP -->
## Roadmap

-I would like to map the users ID to assign users from the document
-I would like to have an attachment to the document for each project

See the [open issues](https://github.com/giterdun345/imServiceProvider/issues) for a list of proposed features (and known issues). Or make a request for a new feature.




<!-- LICENSE -->
## License

Distributed under the GNU License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - John - jketterer@illustrativemathematics.org

Project Link: [https://github.com/giterdun345/imServiceProvider](https://github.com/giterdun345/imServiceProvider)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[issues-shield]: https://img.shields.io/github/issues/giterdun345/repo.svg?style=for-the-badge
[issues-url]: https://github.com/giterdun345/repo/issues
[license-shield]: https://img.shields.io/github/license/giterdun345/repo.svg?style=for-the-badge
[license-url]: https://github.com/giterdun345/repo/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/jm-ketterer
<!-- [heroku-shield]:
[heroku-url]: https://heroku-status-badges.herokuapp.com/immense-plains-50482 -->