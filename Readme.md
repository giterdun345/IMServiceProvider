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
-->

[![LinkedIn][linkedin-shield]][linkedin-url]
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)]

[![Issues/Request][issues-shield]][issues-url]
[![GitHub issues](https://badgen.net/github/issues/Naereen/Strapdown.js/)](https://GitHub.com/giterdun345/imServiceProvider/issues/)

<img src="https://heroku-status-badges.herokuapp.com/immense-plains-50482" alt="server status">

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/giterdun345/imServiceProvider">
    <img src="logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">IM Service Provider</h3>

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
that is scalable, fast, and secure. This project has eliminated the 100 API calls quota, and 30 minute wait time in Workato/Wrike Integrate. Now, IM has greater limits of 500 requests per 100 seconds per project, and 100 requests per 100 seconds per user. There is no wait time reducing the 30 minute wait time to milliseconds. Furthermore, there is also a 100 job limit in Workato. In other words, IM would only be allowed to make 100 API calls based on a trigger for the whole month; this project eliminates any monthly quota.
The project is easy to use and intuitive, so not much to explain in terms of use. 

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
Please do not delete the information in the footer of the document. This is what identifies the data being sent to Wrike and ensure it gets imported to the correct project in Wrike.

To save, click the "Priorities" tab in the menu. Click 'Save to Wrike' to save the data to Wrike.

To change status, click the "Priorities" tab in the menu. Hover over change status; there will be a submenu shown that list the status name. Click the status you wish to change to.

Double click in the text area to input data. When you scroll up and down the document, the cell that you have double clicked will follow you.

If you would like to undo changes made, Press Control + 'Z' to undo changes. 

If you would like to change the size of the document, press Control + '+' to increase the size and press Control + '-' to decrease the size.

You can find the time and date of the last update in the bottom right hand corner of the document in cell 'F117'

You can also find a link to the Wrike project in cell 'F116'

Attachments in the Wrike project are not available in the document, please use the link to navigate back to Wrike to preview, open or download these attachments.

### Troubleshooting
1. I don't see a new document created in Google Drive
  - Make an update in Wrike by making a small change in one of the custom data fields, then check the Drive for a new file

2. My document did not update
  - Please try not to save the document multiple times within 30 seconds. You can but, you could cause the server to be overwhelmed. Or, please check that you did not edit the FolderId value in cell 'B118'

3. I see a green border on my sheet and can't get rid of it.
  - The green border shows you that another user is currently editing that cell.


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
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/jm-ketterer
<!-- [heroku-shield]:
[heroku-url]: https://heroku-status-badges.herokuapp.com/immense-plains-50482 -->