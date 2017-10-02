# Introduction

This little app was written in about an hour to solve several related problems. It is really simple, but it might be useful to you if you give it a chance.

## Example 1: Web service to check for unique username / email on signup.
First, load existing user names into memory by calling http://<host>:7777/load. Then, invoke http://<host>:7777/exists/<key> and you'll get a boolean response.

## Example 2: Get a list of "friends" for a social network.
Just invoke http://<host>:7777/contains/ <prefix> and you'll get a list of user names with partial matches against the search criteria

## Example 3: See who else is online.
In your login code, invoke http://<host>:7777/add/<username>. Now, invoke http://<host>:7777/exists/<key> to look for a specific user, or http://<host>:7777/all or http://<host>:7777/count to get a list of all users logged in or a total count of users logged in.


# Special Sauce
All we've done here is put an http layer on a trie. The trie can be loaded via an http command or from a database. This has some nice features though in that it is
    a) in memory
    b) lets us easily look for partial matches
    c) makes a nice foundation for lots of related problems

This proof-of-concept type application used Tornado Framework, SQL Alchemy, and Datrie (https://pypi.python.org/pypi/datrie/).


# How to Fork Successfully
Here's a list of things you might want to consider, if you intend to use this as an example for your own projects:

 - This app contains no security
 - It uses a simplistic hard-coded User model and works only with usernames. If you want to work with some other attribute, like first name or email address, you'll have to modify it.
 - It uses a simplistic load mechanism, essentially "select * from users;" when http://<host>:7777/load is invoked. Using the metrics from https://pypi.python.org/pypi/datrie/, 100K entries consumes 5MB of ram, so you'll probably not be memory bound. But, if you have 100K users in your users table, it may be a slow load. YMMV.
 - This implementation uses BaseTrie and only cares about the keys of the trie, not the actual values in each node. If you wanted to use this as a general purpose session cache, for example, you'd need to change the underlying trie implementation from BaseTrie to Trie and then insert the appropriate objects into nodes.
 - This app makes no effort to persist its data or recover in the case of crash. If it dies, you'll have to reload your data somehow.
 - Run the test scripts like: "python -m unittest TestSuite" so that you understand how to invoke it.

