# Contributing

* Fork repo
* Make changes (follow commit message guidelines)
* open pull request

## Commit Style

[Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0)
[Git commit message guideline](https://www.freecodecamp.org/news/how-to-write-better-git-commit-messages/)
The Anatomy of a Commit Message
Basic:
`git commit -m <message>`

Detailed:
`git commit -m <title> -m <description>`

5 Steps to Write Better Commit Messages
Let's summarize the suggested guidelines:

Capitalization and Punctuation: Capitalize the first word and do not end in
punctuation. If using Conventional Commits, remember to use all lowercase.
Mood: Use imperative mood in the subject line. Example – Add fix for dark mode
toggle state. Imperative mood gives the tone you are giving an order or request.
Type of Commit: Specify the type of commit. It is recommended and can be even
more beneficial to have a consistent set of words to describe your changes.
Example: Bugfix, Update, Refactor, Bump, and so on. See the section on
Conventional Commits below for additional information.
Length: The first line should ideally be no longer than 50 characters, and the
body should be restricted to 72 characters.
Content: Be direct, try to eliminate filler words and phrases in these
sentences (examples: though, maybe, I think, kind of). Think like a journalist.
How to Find Your Inner Journalist
I never quite thought my Journalism minor would benefit my future career as a
Software Engineer, but here we are!

Journalists and writers ask themselves questions to ensure their article is
detailed, straightforward, and answers all of the reader's questions.

When writing an article they look to answer who, what, where, when, why and ho
. For committing purposes, it is most important to answer the what and why for
our commit messages.

To come up with thoughtful commits, consider the following:

Why have I made these changes?
What effect have my changes made?
Why was the change needed?
What are the changes in reference to?
Assume the reader does not understand what the commit is addressing. They may
not have access to the story addressing the detailed background of the change.

Don't expect the code to be self-explanatory. This is similar to the point
above.

It might seem obvious to you, the programmer, if you're updating something
like CSS styles since it is visual. You may have intimate knowledge on why
these changes were needed at the time, but it's unlikely you will recall why
you did that hundreds of pull requests later.

Make it clear why that change was made, and note if it may be crucial for the
functionality or not.

See the differences below:

`git commit -m 'Add margin'`
`git commit -m 'Add margin to nav items to prevent them from overlapping the
logo'`
It is clear which of these would be more useful to future readers.

Pretend you're writing an important newsworthy article. Give the headline that
will sum up what happened and what is important. Then, provide further details
in the body in an organized fashion.

In filmmaking, it is often quoted "show, don't tell" using visuals as the
communication medium compared to a verbal explanation of what is happening.

In our case, "tell, don't [just] show" – though we have some visuals at our
disposal such as the browser, most of the specifics come from reading the
physical code.

If you're a VSCode user, download the Git Blame extension. This is a prime
example of when useful commit messages are helpful to future developers.

This plugin will list the person who made the change, the date of the changes,
as well as the commit message commented inline.

Imagine how useful this could be in troubleshooting a bug or back-tracing
changes made. Other honorable mentions to see Git historical information are
Git History and GitLens.

Conventional Commits
Now that we've covered basic commit structure of a good commit message, I'd
like to introduce Conventional Commits to help provide some detail on creating
solid commit messages.

At D2iQ, we use Conventional Commit which is a great practice among
engineering teams. Conventional Commit is a formatting convention that
provides a set of rules to formulate a consistent commit message structure
like so:

```gitcommit
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

The commit type can include the following:

**feat** – a new feature is introduced with the changes
**fix** – a bug fix has occurred
**chore** – changes that do not relate to a fix or feature and don't modify src or
test files (for example updating dependencies)
**refactor** – refactored code that neither fixes a bug nor adds a feature
**docs** – updates to documentation such as a the README or other markdown files
**style** – changes that do not affect the meaning of the code, likely related to
**code** formatting such as white-space, missing semi-colons, and so on.
**test** – including new or correcting previous tests
**perf** – performance improvements
**ci** – continuous integration related
**build** – changes that affect the build system or external dependencies
**revert** – reverts a previous commit
The commit type subject line should be all lowercase with a character limit to
encourage succinct descriptions.

The optional commit body should be used to provide further detail that cannot
fit within the character limitations of the subject line description.

It is also a good location to utilize `BREAKING CHANGE: <description>` to note
the reason for a breaking change within the commit.

The footer is also optional. We use the footer to link the JIRA story that
would be closed with these changes for example: `Closes D2IQ-<JIRA #>` .

Full Conventional Commit Example

```gitcommit
fix: fix foo to enable bar

This fixes the broken behavior of the component by doing xyz. 

BREAKING CHANGE
Before this fix foo wasn't enabled at all, behavior changes from <old> to <new>

Closes D2IQ-12345
```

To ensure that these committing conventions remain consistent across developer
, commit message linting can be configured before changes are able to be
pushed up. Commitizen is a great tool to enforce standards, sync up semantic
versioning, along with other helpful features.

To aid in adoption of these conventions, it's helpful to include guidelines
for commits in a contributing or README markdown file within your projects.

Conventional Commit works particularly well with semantic versioning (learn
more at SemVer.org) where commit types can update the appropriate version to
release. You can also read more about Conventional Commits here.

Commit Message Comparisons
Review the following messages and see how many of the suggested guidelines
they check off in each category.

Good

```gitcommit
feat: improve performance with lazy load implementation for images
chore: update npm dependency to latest version
Fix bug preventing users from submitting the subscribe form
Update incorrect client phone number within footer body per client request
```

Bad

```gitcommit
fixed bug on landing page
Changed style
oops
I think I fixed it this time?
empty commit messages
```
