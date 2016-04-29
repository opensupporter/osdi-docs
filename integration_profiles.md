---
layout: default
title: Integration Profiles
---

# Integration Profiles

This document defines common integration profiles. Integration profiles define a common integration scenario between two types of OSDI systems.


### Sections

* [What Are Integration Profiles?](#what-are-integration-profiles)
* [List Of Profiles](#list-of-profiles)

## What Are Integration Profiles?

Integration profiles attempt to define common scenarios and sets of API calls describing certain types of integrations between two OSDI systems.

For example, let's say you are a fundraising tool that wants to integrate with a digital organizing platform that uses OSDI. The point of the integration would be to store fundraising data you collect in your tool (such as who donated and how much) in the digital organizing system, so users of both of your systems could have access to fundraising data collected in your tool in the digital organizing system they also use, allowing them to target emails to people who donated to them in your tool.

Assuming the digital organizing system you're integrating with supports the relevant OSDI API calls, you could accomplish this integration by implementing the [fundraising integration profile](fundraising_profile.html) -- a set of API calls you can make to store fundraising data from your tool in the digital organizing system.

In this way, integration profiles aim to help you as an implementer string together the chain of calls needed to accomplish common tasks. If an OSDI system supports a certain profile, then all you need to do to integrate in that way is implement the profile yourself.

## List Of Profiles

* [Fundraising Profile](fundraising_profile.html)
* [List Exchange Profile](list_exchange_profile.html)