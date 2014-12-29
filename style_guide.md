---
layout: default
title: Resource Name
---

# OSDI Style Guide

When writing documentation for the OSDI specification, please follow the following procedure and conventions to keep the documentation uniform.

## General overview

The OSDI specification is written in Markdown and outputted with Jekyll to static HTML pages. We make use of Jekyll includes for commonly used text. Examples are written in JSON, with four spaces used for tabs.

## Writing Documentation

### Step 1: Copy resource-template.md

The ```resource-template.md``` file in the ```gh-pages``` branch is a template OSDI resource documentation page designed to make your writing process easier. It contains the standard sections, includes, and semantic layout that you should use on every resource documentation page. Some resources or pages may require a different format, but generally the template should be followed as closely as possible.

Make a copy of the template file and rename it to the name of the resource you are documenting to get started.

### Step 2: Write your documentation

Using the template, write the documentation for your resource, making sure to fill in the necessary information for each section. Familiarize yourself with the includes used in the template, so you are not repeating what's already been said accidentally.

Full sentances are preferred, with appropriate punctuation. For example, field descriptions should be full sentances. Capitalize the resource name if it is referred to as a resoure. For example, "The Person resource represents the fields for a person" should be capitalized, where "Update a person by posting to their endpoint" should not be capitalized.

### Step 3: Craft your examples

While the field tables at the top of your documentation serve as the canonical representation of the resource, the examples below should be carefully crafted, as they are often the most useful part of the documentation for implementers.

The template file shows the standard CRUD (Create, Read, Update, Delete) examples that most resources should have, including two GET examples, one for collections and one for individual resources. However, you may have use for other examples for your resource, and some of the CRUD examples may not make sense in context. For example, when documenting a helper, the create (POST) example is all you really need.

Generally, try to show the full CRUD examples where appropriate, and make sure to include others to fully show off the functionality of the resource. In addition, make sure each example shows enough data and fields so that each part of the field tables above is shown at least once, to ensure an example is given for every field and operation we support. Feel free to include comments such as ```//truncated for brevity``` where appropriate (such as showing only two resources in a collection instead of a larger number), but ensure you are covering each field fully with an example.

Finally, make sure your examples are internally consistent -- use the same IDs, field values, and other details throughout to fully show how examples would work in practice.


### Step 4: Validate your code

When you are finished writing, make sure to validate your code in all of these ways:

* Spell check your document to catch spelling errors.
* Make sure your example JSON is valid with [jsonlint.com](http://jsonlint.com/) or a similar tool
* Make sure your example JSON uses four spaces for each tab stop
* Check all links, including internal anchors and cross-document links
* Take a good look at the Jekyll output after your commit to ensure everything looks visually correct


### Step 5: Add appropriate links

Now that you're done with your new documentation page, please search through other documentation pages and create links to your new page where appropriate. For example, field tables that reference your newly created resource page should be linked.