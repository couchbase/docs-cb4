# Contributing to Couchbase Server Documentation
First of all, thanks for taking the time and effort to contribute!

The following is a short guide for contributing to the Couchbase Server documentation.

## Reporting Bugs and Requesting Enhancements
All bugs and enhancements for the Couchbase Server documentation are tracked via the [DOC project](https://issues.couchbase.com/projects/DOC/issues) on https://issues.couchbase.com. 
If you have found a bug or think there is room for improvement please don't keep it to yourself, even if you don't intend to make the change yourself!
Raise a DOC bug and it will get looked at by someone.

You can also raise DOC bugs on specific pages using the 'Feedback On This Page?' button in the bottom-right of any page on https://developer.couchbase.com. 

### How do I submit a (Good) DOC bug?
- __Use a clear and descriptive title__ - e.g `Instructions for disabling THP on RHEL/Centos 7 and later do not work`
- __Describe the problem or enhancement in full__ - for any problem, please
include the problem in detail, including any expected results and how they
differ from the real results. Please remember that the documentation team are not experts in every individual aspect of Couchbase
and so may not fully understand the issue. For that reason, try to be as descriptive as possible, providing the correct text or command
(if you know it). This will drastically speed up the time taken to resolve the issue.
https://issues.couchbase.com/browse/DOC-2056 is a good example of a well-written DOC bug which allowed the writer to make the necessary changes very quickly.

## Contributing Changes
If you feel confident in contributing the changes to resolve an issue yourself then this is greatly encouraged!

### Style Guide

Below is a basic style guide that we try to follow throughout our entire documentation:
- Write in the present tense (that means say "something does whatever" rather than "something will do whatever").
- Write in the second person (that means address your readers directly as you, and do not use I, or we, our, or one).
- Use active voice (not passive). For example:
  - active: The dog ate the bone.
  - passive: The bone was eaten by the dog
- Write clearly and concisely. Check sentences with more than 25 words to see if you can split them for clarity.
- Use plain language. Don’t use formal or long words when easy or short ones will do. Use buy instead of purchase, help instead of assist, about instead of approximately, and so on.
- Use consistent terminology (that means this isn't creative writing so you don't need to describe the same thing differently every time you mention it).
- Write in American English (spelling and word usage).
- Use parallel structure in lists (that means use the same sentence pattern for each item). If your list is made up of fully formed sentences then they should end with full stops.
- Spell out acronyms and include them in parentheses the first time they are used in a document, ex. General Motors (GM). Common acronyms like noSQL don’t require spelling out.
- Use contractions (such as can’t and won’t).
- Use simple sentences.
- Use short paragraphs.
- Use title case for titles and headings (that means capitalize all the significant words, leave words like to, and, and for in lowercase).
- Avoid using specific version numbers whenever possible. Don't say Couchbase Server 4.0 ..., instead you can just say Couchbase Server.

### Workflow 

#### Working with DITA

Currently, the documentation is written in a markup language called [DITA](https://docs.oasis-open.org/dita/v1.2/cs01/spec/archSpec/ditamarkup.html).
This is an xml-based language and provides a lot of benefits such as lack of ambiguity and ability to re-use and cross-reference content easily.

Usually this is a language that is unfamiliar to most people who may have previously used markdown, a short primer can be found at http://www.publishingsmarter.com/resources/books-and-articles/dita-primer-learn-dita
if you want to make a start. Of course you can also ask questions to any of the members of the documentation team if you need help (can be done via GitHub issues or the Pull Requests themselves).

Another issue that many people have is working out which file they need to change based on the web page that they will to change.
DITA makes this very easy as there is a 1-1 mapping between the dita files and the generated html.
For example, https://developer.couchbase.com/documentation/server/4.5/install/install-platforms.html maps to the file `content/install/install-platforms.dita` on the branch `4.5`.
Usually a bot will post in any raised DOC bugs stating which file needs to be updated.

[Oxygen XML Author](https://www.oxygenxml.com/xml_author.html) is an excellent tool for editing and creating content in DITA and is highly recommended
if you would prefer to work with a WYSIWYG editor. Once you are familiar with the dita syntax it is also easy to create content directly in the dita xml.

Before submitting changes you should ensure that your content builds successfully following the build instructions in the readme.

##### FOR COUCHBASE EMPLOYEES

We currently have a version of Oxygen Web Author running, you can use this to edit your DITA files - a short guide on how to use the tool can be found on [the wiki](http://hub.internal.couchbase.com/confluence/display/techpubs/Using+Oxygen+Web+Author).

#### Git
Due to write restrictions it is preferred if you first create your own fork of this repository and make all of your changes in this forked repository, using Pull
requests to merge changes from the fork to the main repository.

Setting up a fork is easy, just press the 'Fork' button in the top-right of the repository.

Once you have your own fork, you are ready to make changes.

A common workflow can be found below

```
# Only required when first setting up the local repo
git clone https://github.com/<your-user>/docs-cb4.git

cd docs-cb4

BRANCH=DOC-XXXX
# Ensure that we base our changes on master
git checkout master 
# Creates a new branch with the desired name
git branch $BRANCH 

# Creates the branch on your remote repo
git push origin $BRANCH

# Checks out the newly created branch
git checkout $BRANCH

# Edit the files in question

# Add the edited files to be committed
git add my_files

# Commit the edited files
git commit -m "DOC-XXXX: Created git workflow example"

# Push the updated changes to your remote repository
git push origin $BRANCH
```

#### Pull Requests
Once your changes are in a branch on GitHub it is time to submit them to the main couchbase repository.

This is done using pull requests, you can read more about pull requests in general at https://help.github.com/articles/creating-a-pull-request/.

This section will focus on what happens once you have created your pull request from your fork's branch onto the master branch.

1. As soon as your pull request has been submitted, the continuous integration will trigger, this can be seen as the check 'PR-Build'.
This builds the entire documentation set including your changes to ensure that it builds successfully (thus preventing malformed dita from breaking master).
Once it has done this it will report back whether or not it was successful, along with a link to a preview of any pages which have been updated in the PR.
You can use these links to see what your changes will look like (and whether or not you think you need further changes). Every time the content of the PR 
is updated, this will retrigger.

2. A member of the documentation team will then review your pull request and let you know if any changes are required. Usually you will be asked to make any
necessary changes yourself. Don't worry if you're asked to make changes, this is normal!

3. Once the reviewer is happy with the changes, they will backport them to any necessary branches (please let them know if you think it needs backporting to certain releases)
and merge your changes.

#### Changes on the Site
Changes are not immediately pushed to the live site (developer.couchbase.com), usually the most recent versions are pushed to production twice a week, so you may need to wait
a few days to see your changes reflected.
