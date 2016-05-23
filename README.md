# Couchbase Documentation

The Couchbase Documentation Repository for Couchbase 4+ DITA based Docs

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

## Generating Documentation

Docs are generated with DITA OT. Technically, we have a [forked
version](https://github.com/couchbaselabs/dita-ot-2.1.1) of DITA OT.
As of this writing, we know this exists but we don't quite know why it
was forked and it was done without history.  That's a todo for later.

Generating docs is done like this:
```
dita -f html5 -i cb-docs.ditamap -o ~/tmp/output/
```

