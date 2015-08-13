---
layout: default
title: "OSDI"
---

<center>
<img src="http://opensupporter.org/wp-content/themes/osdiv2/images/site/osdi-logo.png" alt="OSDI" />
</center>

-----------------------------
This document defines common integration profiles.  Integration profiles define a common integration scenario between two types of OSDI systems.  

### Sections

* [Mobile Telephony to CRM](#mobile-telephony)
* [Field Organizing System](#field-organizing)

### Mobile Telephony

#### Inbound Pull
The Mobile Telephony System (MTS) system will pull information on mobile subscribers from an OSDI CRM using:

1. find 'mobile subscribers' OData query 
2. Oauth or API Key
3. Multiple record, paged data query (person collection)

#### Outbound supporter push
The MTS will push updated supporter data to an OSDI CRM using:

1. person_signup_helper
2. Custom Fields
3. Action History
4. Canvassing Interactions

### Field Organizing

A Field Organizing System (FOS) has two types of integrations.  

1. Inbound Pull - Pulls supporter data from CRMs into FOS store to perform survey Q&A
2. Outbound Push - With survey Q&A responses captured, the system will push that data into CRMs.  There are multiple possible modes such as custom fields, or Q&A.  Custom fields is the initial scenario.


#### Inbound Pull
To integrate, the following are needed

1. Lists of Lists 
2. Oauth or API Key
3. Multiple record, paged data query (person collection)

#### Outbound push
The FOS will push supporter data into a CRM with:

1. person_signup_helper
2. custom fields support

#### Ephemeral Requirements

1. sandbox environment for prototyping / testing