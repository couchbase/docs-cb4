This is the analytics documentation set.

While we are in the integration stage of analytics with Couchbase
Server, the documentation is split. Some CB-specific files are 
written in dita like the rest of the documentation, however there
are also some files taken from the upstream AsterixDB project -
https://github.com/apache/asterixdb. Unfortunately these files
are written in markdown and so require a little extra work to
work with the existing documentation system.

To resolve this we use jekyll to generate the markdown files into
html and then add these raw html files to the ditamap.
Below are a concise set of steps to convert the markdown files to
html and add them to the documentation set.

## Install Jekyll
1. Install ruby - https://www.ruby-lang.org/en/documentation/installation/
2. Ensure that all of the appropriate ruby binaries are in your $PATH
3. Install jekyll:
```
gem install jekyll bundler
```

## Add the Markdown File
1. Make a local copy of the markdown file which you wish to convert
2. Move or copy this file to `docs-cb4/content/analytics/html_generation`
3. If you are updating an existing html file, ensure that your markdown 
file has the same name as the generated html. e.g. to update my_example.html
the markdown file should be named my_example.md.
4. Add the necessary FrontMatter to your markdown file. This is the short 
yaml section at the beginning of the markdown file, for example (taken
from `example.md`):
```
---
title: Example Title
description: Example Description
layout: default
---
```
**The layout should not be changed from default, or the html generation
will not function correctly**

5. The .gitignore is configured to ignore any markdown files in this directory,
you should not commit the markdown file as part of your change.

## Generate the HTML
1. Navigate to the `html_generation` directory where your markdown files are
located.
2. Build the markdown files using the following command:
```
jekyll build
```
3. The generated html files will then be located in the `_sites` directory.

## Add the HTML Files
1. Now that the html has been generated, you will want to copy the relevant
html files to the `content/analytics/` directory, overwriting any existing
html files if you are updating existing content.
2. If you're adding new pages then add the html page to the `analytics.ditamap`
located in `content/analytics/`, inside the 'SQL++ topichead. 
The format for doing so is as-follows:
```
<mapref href="my_example.html" format="html" navtitle="my nav title"/>
```
3. Commit the updated ditamap and any updated html files.
