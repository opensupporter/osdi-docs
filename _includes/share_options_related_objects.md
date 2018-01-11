#### Share Options

|Name          |Type      |Description
|-----------    |-----------|--------------
|facebook_share	|[Facebook Share](#facebook-share)    |An object hash representing the default language and attributes used when an activist shares on Facebook.
|twitter_share	|[Twitter Share](#twitter-share)    |An object hash representing the default language and attributes used when an activist shares on Twitter.
|email_share	|[Email Share](#email-share)    |An object hash representing the default language and attributes used when an activist shares via email.

#### Facebook Share

|Name          |Type      |Description
|-----------    |-----------|--------------
|facebook_share.title |string    |The title of the post created when an activist shares content on Facebook.
|facebook_share.description |string    |The description of the post created when an activist shares content on Facebook.
|facebook_share.image |string    |The URL of an image that goes with post created when an activist shares content on Facebook.
|facebook_share.total_shares		|integer	|A computed property representing the current count of the total number of times the content has been shared on Facebook.
|facebook_share.share_url		|string        	|A URL string pointing to the page that is used specifically for Facebook sharing

#### Twitter Share

|Name          |Type      |Description
|-----------    |-----------|--------------
|twitter_share.message |string    |The text of the post created when an activist shares content on Twitter. Some systems may use templating or appends to insert the `share_url` into the tweet automatically.
|twitter_share.total_shares		|integer	|A computed property representing the current count of the total number of times the content has been shared on Twitter.
|twitter_share.share_url		|string        	|A URL string pointing to the page that is used specifically for Twitter sharing

#### Email Share

|Name          |Type      |Description
|-----------    |-----------|--------------
|email_share.subject |string    |The subject line of the email created when an activist shares content via email.
|email_share.body |string    |The body text of the email created when an activist shares content via email. Some systems may use templating or appends to insert the `share_url` into the email body automatically.
|email_share.total_shares		|integer	|A computed property representing the current count of the total number of times content has been shared via email.
|email_share.share_url		|string        	|A URL string pointing to the page that is used specifically for email sharing