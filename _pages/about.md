---
permalink: /
title: "About me"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

* This website is a work in progress, updates coming gradually. *

I am a postdoc at the Kavli Institute for Particle Astrophysics and Cosmology (KIPAC) at Stanford University. I'm interested in using cosmological observations to better understand and constrain fundamental physics, and in studying how we can get as much information as possible out of those observations. I'm also interested in science outreach and in making STEM fields more accessible and welcoming to everyone.

Bio
======

A native Michigander, I grew up in a suburb of Detroit (Romeo) and received my undergraduate degree from Michigan State University. I spent two years at the University of Cambridge as a Marshall Scholar where I completed Part III of the Mathematical Tripos and spent a year working on research on modified gravity with Professor Anne-Christine Davis. I did my PhD in the University of Michigan's [Department of Physics](http://www.lsa.umich.edu/physics), where I worked with [Professor Dragan Huterer](http://www-personal.umich.edu/~huterer/cosmo_website/people.html) as part of the Michigan cosmology group.  



Current and recent projects
======

* **Beyond standard-model cosmology for DES Year 3** -  The [Dark Energy Survey (DES)](https://www.darkenergysurvey.org/) is an ongoing project to map the distribution of matter in 1/8th of the sky, and to use the information gathered from that survey to place constraints on, among other things, dark energy properties. With [Agnes Ferte](https://science.jpl.nasa.gov/people/Ferte/) I am co-leading the DES analysis team that will be using Year 3 data to constrain a set of simple extensions to our standard cosmological model, including dynamic dark energy, non-flat geometry, sterile neutrinos, and modified gravity. 

* **Blinding for the DES analysis** - DES and other modern cosmological experiments aim to make more and more precise measurements to constrain cosmological paramters, and to use those constraints to test our standard cosmological model, LCDM. In doing this, we either look at how parameters describing possible new physics compare to their LCDM values, or how the results of different experiments compare to one another. We want to ensure that the many decisions requrired to go from raw observables to parameter estimation, are not influenced (even unconsciously) by how the results of the analysis compare to the experimenters' expectations. One  tool we can use to prevent experimenter bias from influencing the results of precise cosmological analyses is to blind the analysis, or to modify the data in some way that changes the output of parameter estimation. This is challenging to do for DES, as its analysis relies on the analysis of many different observable probes. I am leading the development and validation of a method  blind multi-probe cosmology analyses by modifying summary statistics, namely the two-point correlation functions for galaxy clustering and weak lensing. 


* **Growth-geometry split analysis of DES data** - Many models of modified gravity can produce the same expansion history as $\Lambda$CDM, the standard cosmological model of a cosmological constant + cold dark matter + general relativity, but will differ in their predictions for structure growth. The idea of the grow-geometry split analysis is to separately constrain the LCDM parameters using probes of expansion and structure growth, and then to use the comparison of those constraints as a consistency test of LCDM. I'm currently implementing and testing a pipeline to run this kind of analysis on the Year-1 data for DES. I'm also generally interested in using galaxy survey data to test for modified gravity via phenomenological parameterizations of deviations from general relativity.

* **CMB anomaly covariances** - For the most part, data from the CMB have been found to be in remarkable agreement with the predictions of LCDM. However, there are a handful of features on very large angular scales which are statistically unlikely in LCDM, which have been the subject of much study. I used ensembles of simulated skies to characterize the extent to which these various anomalies are independent and published the results in [this paper](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.98.023521).

* ISW signal reconstruction - The integrated Sachs-Wolfe (ISW) effect is a result of the fact that the energy of cosmic microwave background (CMB) photons gets modulated when pass through gravitational potential wells associated with large scale structure (LSS) on their way from the surface of last scattering to us. This energy modulation contributes to CMB temperature anisotropies at large angles. One can use theoretical cross correlations and maps of LSS tracers to try to reconstruct a map of the ISW signal. In two  papers ([here](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.94.043503) and [here](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.97.043515)), I explored how different survey properties and systematics affecting the input galaxy maps impacted the accuracy of this kind of ISW signal reconstruction.



<!---
Like many other Jekyll-based GitHub Pages templates, academicpages makes you separate the website's content from its form. The content & metadata of your website are in structured markdown files, while various other files constitute the theme, specifying how to transform that content & metadata into HTML pages. You keep these various markdown (.md), YAML (.yml), HTML, and CSS files in a public GitHub repository. Each time you commit and push an update to the repository, the [GitHub pages](https://pages.github.com/) service creates static HTML pages based on these files, which are hosted on GitHub's servers free of charge.

Many of the features of dynamic content management systems (like Wordpress) can be achieved in this fashion, using a fraction of the computational resources and with far less vulnerability to hacking and DDoSing. You can also modify the theme to your heart's content without touching the content of your site. If you get to a point where you've broken something in Jekyll/HTML/CSS beyond repair, your markdown files describing your talks, publications, etc. are safe. You can rollback the changes or even delete the repository and start over -- just be sure to save the markdown files! Finally, you can also write scripts that process the structured data on the site, such as [this one](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.ipynb) that analyzes metadata in pages about talks to display [a map of every location you've given a talk](https://academicpages.github.io/talkmap.html).

Getting started
======
1. Register a GitHub account if you don't have one and confirm your e-mail (required!)
1. Fork [this repository](https://github.com/academicpages/academicpages.github.io) by clicking the "fork" button in the top right. 
1. Go to the repository's settings (rightmost item in the tabs that start with "Code", should be below "Unwatch"). Rename the repository "[your GitHub username].github.io", which will also be your website's URL.
1. Set site-wide configuration and create content & metadata (see below -- also see [this set of diffs](http://archive.is/3TPas) showing what files were changed to set up [an example site](https://getorg-testacct.github.io) for a user with the username "getorg-testacct")
1. Upload any files (like PDFs, .zip files, etc.) to the files/ directory. They will appear at https://[your GitHub username].github.io/files/example.pdf.  
1. Check status by going to the repository settings, in the "GitHub pages" section

Site-wide configuration
------
The main configuration file for the site is in the base directory in [_config.yml](https://github.com/academicpages/academicpages.github.io/blob/master/_config.yml), which defines the content in the sidebars and other site-wide features. You will need to replace the default variables with ones about yourself and your site's github repository. The configuration file for the top menu is in [_data/navigation.yml](https://github.com/academicpages/academicpages.github.io/blob/master/_data/navigation.yml). For example, if you don't have a portfolio or blog posts, you can remove those items from that navigation.yml file to remove them from the header. 

Create content & metadata
------
For site content, there is one markdown file for each type of content, which are stored in directories like _publications, _talks, _posts, _teaching, or _pages. For example, each talk is a markdown file in the [_talks directory](https://github.com/academicpages/academicpages.github.io/tree/master/_talks). At the top of each markdown file is structured data in YAML about the talk, which the theme will parse to do lots of cool stuff. The same structured data about a talk is used to generate the list of talks on the [Talks page](https://academicpages.github.io/talks), each [individual page](https://academicpages.github.io/talks/2012-03-01-talk-1) for specific talks, the talks section for the [CV page](https://academicpages.github.io/cv), and the [map of places you've given a talk](https://academicpages.github.io/talkmap.html) (if you run this [python file](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.py) or [Jupyter notebook](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.ipynb), which creates the HTML for the map based on the contents of the _talks directory).

**Markdown generator**

I have also created [a set of Jupyter notebooks](https://github.com/academicpages/academicpages.github.io/tree/master/markdown_generator
) that converts a CSV containing structured data about talks or presentations into individual markdown files that will be properly formatted for the academicpages template. The sample CSVs in that directory are the ones I used to create my own personal website at stuartgeiger.com. My usual workflow is that I keep a spreadsheet of my publications and talks, then run the code in these notebooks to generate the markdown files, then commit and push them to the GitHub repository.

How to edit your site's GitHub repository
------
Many people use a git client to create files on their local computer and then push them to GitHub's servers. If you are not familiar with git, you can directly edit these configuration and markdown files directly in the github.com interface. Navigate to a file (like [this one](https://github.com/academicpages/academicpages.github.io/blob/master/_talks/2012-03-01-talk-1.md) and click the pencil icon in the top right of the content preview (to the right of the "Raw | Blame | History" buttons). You can delete a file by clicking the trashcan icon to the right of the pencil icon. You can also create new files or upload files by navigating to a directory and clicking the "Create new file" or "Upload files" buttons. 

Example: editing a markdown file for a talk
![Editing a markdown file for a talk](/images/editing-talk.png)

For more info
------
More info about configuring academicpages can be found in [the guide](https://academicpages.github.io/markdown/). The [guides for the Minimal Mistakes theme](https://mmistakes.github.io/minimal-mistakes/docs/configuration/) (which this theme was forked from) might also be helpful.
--->