# Git Github Gitlab
#### What is git, github, gitlab

---

# What is Source code control

It is important to manage your code in terms of history and managing versions and allow multiple prople contribute to the code. It aids in project management.

There are different types of version control systems:
* centralized 
* distributed

Centralized version control framework examples are SVN,  CSV. There's a central place where all the files is kept.

The local file system will all be read-only and users must execute 'check-out' operation to edit the file. If someone already checked out the file, one must wait until the files are checkedin.

Few disadvantages of centralized systms are that it has a single point of failure. If this goes down, nobody can work on the system. So this is not a very preferred situation.

Now in a distributed version control systems, everybody has a copy of the repository. So like this, remote repository which contains all the data in the file. And if somebody wants to work on it, let's say developer 1, he just makes a copy of it. Technically in GitHub, we call it clone. So he just take a snapshot of the whole remote repository.

Similarly, developer 2, if he wants to work on that, he just takes the whole copy of the remote repository. It's called again cloning, as we'll see in detail. And there's no dependency. Remote site can be down. I can still work on my code because I have a complete snapshot of it.

And once I'm done, I can go ahead and start sharing my work with some other. And I have to somehow sync with the remote repository and my repository and with other developer repository also, which is taken care of by tools in the distributed version control system. So it's nice because there's not a single point of failure. But one thing you can see, that if it has a lot of data cloning can take a lot of time.

So one of the most popular distributed version control system is GitHub, or Git tools. It's very popular. We'll go over detail on this one.

Some git commands

git config --global user.name  'your-name'
git config --global user.email 'your-email'
git config --list # show all git congfiguration

---‣
