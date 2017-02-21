# Couchbase Documentation

The Couchbase Documentation Repository for Couchbase 4+ DITA based Docs

### Contributing
A guide for contributing to the Couchbase Server Documentation can found be 
[here](CONTRIBUTING.md).

### HTML ID tags
All major content within the documentation should be annotated with ID
tags to allow linking to specific sections of content within the
documentation.  These ID tags should match the title of the section,
they must use alpha-numeric lower-case characters only and any spaces
must be replaced with underscores.

### Code Samples
Inclusion of code samples is an important aspect of our documentation.
Code-samples within our documentation should be commited to the
devguide-examples repository, and then the same code should be
included within the documentation directly as a code block.  These
code-blocks should have a comment on the first line indicating the
source of the code (in the format of a link to the specific file and
lines on github).  It is the responsibility of the person who changes
a code sample to update all links to that code sample file.  Note that
the devguide-examples has a branch per major.minor version of the
documentation starting with 4.5.

## Rules on Content
Make sure all topics have a short description, as that is used not only
to inform the reader about what is in this document, but it also goes
in the `meta` description in the HTML.  Google may use this as the
snippet under a link in a search result.  They recommend "a page's
description meta tag might be a sentence or two or a short paragraph"

An anti-example:
> This section bootstraps knowledge on completely asynchronous
computations using the SDK."

Replaced with:
> The Couchbase Java SDK has a complete asynchronous API based in part
on RxJava. This section provides information on how the asynchronous
API can be used, how it works with Java platform and RxJava features
and the kinds of error handling you will need to consider in application
development.

That may even be a little long, but this was for a long page.  Note that
it gets in keywords like Java and RxJava.

## Generating Documentation

Docs are generated with DITA OT. Technically, we have a [forked
version](https://github.com/couchbaselabs/dita-ot-2.1.1) of DITA OT.
As of this writing, we know this exists but we don't quite know why it
was forked and it was done without history.  That's a todo for later.

Generating docs is done like this:
```
dita -f html5 -i cb-docs.ditamap -o ~/tmp/output/ -Deditlink.remote.ditamap.url=https://github.com/couchbase/docs-cb4/edit/master/content/cb-docs.ditamap
```

