# Couchbase Documentation

The Couchbase Documentation Repository for Couchbase 4+ DITA based Docs

### Contributing
A guide for contributing to the Couchbase Server Documentation can be found 
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

Code samples typically come in three flavors:
1. One-liners, for example
   
   ```
   cb.upsert(docid, {'key1': 'value1'})
   ```
   
   This kind of example hints at proper usage, but does not entirely reflect what the operation does.
   it is understood that the text surrounding the example provides sufficient explanation
2. Contextual, for example
   
   ```
   rv = cb.upsert(docid, {'key1': 'value1'}
   print rv
   # <OperationResult>...
   ```
   
   This kind of example might provide some additional information at how a specified API or
   operation works, and how it might be used in application code. The example is syntactically
   correct, but may not include all the required components for making it functional.
3. Standalone, for example
   
   ```
   from couchbase.bucket import Bucket
   cb = Bucket('couchbase://localhost/default')
   rv = cb.upsert(docid, {'key1': 'value1'}
   print rv
   # ...
   ```
   
   This is a fully functional, standalone example which can be executed by a user. This may
   contain a significant amount of boilerplate (such as imports and other initialization code)
   needed to make the example standalone.

Examples of the standalone kind will live inside the [devguide-examples](https://github.com/couchbaselabs/devguide-examples) repository. These examples _should_ be copied over to DITA where necessary, but should be modified to be contextual so as not to confuse the reader. A link to the standalone example should be placed near the contextual example, so that a user may be able to further execute and play with the code.

There are no strict rules for where to place examples and what type they should be.

One-liners do not need to be sourced in real code, and are more similar to pseudocode (but are syntactically correct for the language being used).

The content in the devguide-examples repository is versioned by server version (TODO: how to version by SDK version? or perhaps just version that inside the filename?).

Documentation authors (i.e. SDK maintainers) should ensure that in-dita links to the examples refer to the versioned branches, and that fixes in documentation are reflected in both standalone and contextual examples

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

