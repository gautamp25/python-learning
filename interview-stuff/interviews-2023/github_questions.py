"""
    Explain the purpose of version control systems. How does Git differ from other version control systems, and why is it widely used in the industry?

    Describe your experience with Git. How do you typically structure your commits? Do you follow any particular branching strategy?

    What is the difference between Git and GitHub? How does GitHub enhance collaboration in a software development project?

    Explain the concept of forking a repository on GitHub. When would you fork a repository, and how do you keep your forked repository in sync with the original?

    Discuss Git branching strategies. What is the Git flow, and how does it help in managing feature development, releases, and hotfixes?

    How do you handle merge conflicts in Git? Can you explain the steps you take to resolve conflicts during a merge or rebase operation?

    Describe the purpose and use of a pull request in GitHub. What information and discussions do you include in a pull request, and how do you review someone else's pull request?

    Explain the difference between a Git commit and a GitHub commit. How do you push changes to a remote repository on GitHub?

    What are GitHub Actions, and how can they be utilized in a software development workflow? Provide examples of scenarios where GitHub Actions might be beneficial.

    Discuss the importance of README files in GitHub repositories. What information should be included in a good README, and how does it contribute to project documentation?

    Have you used GitHub Pages? Explain how it works and provide an example of a project where you utilized GitHub Pages for documentation or hosting.

    What is a GitHub repository's Wiki? How do you use it for additional project documentation, and what are the benefits of maintaining a Wiki?

    Describe your experience with GitHub projects or project boards. How do you organize and manage tasks using GitHub project management features?

    Have you integrated GitHub with any third-party tools or services? For example, CI/CD tools, code quality analysis, or issue tracking systems.

    How do you handle code reviews on GitHub? What criteria do you consider when reviewing someone else's code, and how do you provide constructive feedback?
"""

"""
git merge and git rebase are two different Git commands used for integrating changes from one branch into another. They have different approaches to combining changes and offer distinct advantages and use cases. Here's a brief overview of the differences:

    git merge:
        Purpose: The primary purpose of git merge is to integrate changes from one branch into another.
        Process: When you run git merge, Git creates a new commit that has two parent commits—the latest commit on the current branch and the latest commit on the branch being merged.
        Commit History: The commit history remains linear, and the branch being merged in retains its commit history.
        Advantages:
            Simple and straightforward.
            Preserves the commit history of both branches.

    bash

# Example of merging 'feature-branch' into 'main'
git checkout main
git merge feature-branch

git rebase:

    Purpose: The primary purpose of git rebase is to combine a sequence of commits into a new base commit.
    Process: When you run git rebase, Git identifies the common ancestor commit of the current branch and the branch you are rebasing onto. 
    It then replays the changes from the current branch on top of the other branch, creating a new, linear commit history.
    Commit History: The commit history becomes linear, and it appears as if the changes were made directly on top of the other branch.
    Advantages:
        Creates a cleaner, linear history.
        Reduces the number of merge commits.

bash

    # Example of rebasing 'feature-branch' onto 'main'
    git checkout feature-branch
    git rebase main

When to Use Each:

    Use git merge when you want to preserve the original commit history, and a merge commit accurately represents the integration of changes from one branch to another.
    Use git rebase when you want to maintain a cleaner, more linear commit history. This is often preferred for feature branches that are still in progress before being merged into the main branch.

Important Note:

    Never rebase commits that you have already pushed to a shared repository. Rewriting history with git rebase can cause conflicts for collaborators who have pulled the old history, leading to potential issues.

In summary, the choice between git merge and git rebase depends on your preference for commit history aesthetics and the specific requirements of your project.
"""