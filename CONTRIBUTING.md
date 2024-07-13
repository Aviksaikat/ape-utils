# Development

To get started with working on the codebase, use the following steps prepare your local environment:

```bash
# clone the github repo and navigate into the folder
git clone https://github.com/Aviksaikat/ape-utils.git
cd ape-utils

# create and load a virtual environment
hatch env create

# install the developer dependencies and run a shell
hatch shell
```

## Pre-Commit Hooks

We use [`pre-commit`](https://pre-commit.com/) hooks to simplify linting and ensure consistent formatting among contributors.
Use of `pre-commit` is not a requirement, but is highly recommended.

Install `pre-commit` locally from the root folder:

```bash
pip install pre-commit
pre-commit install
```

Committing will now automatically run the local hooks and ensure that your commit passes all lint checks.

## Issue Reports

If you experience bugs or general issues with `ape-utils`, please have a look
on the [issue tracker].
If you don't see anything useful there, please feel free to fire an issue report.

!!! tip
    Please don't forget to include the closed issues in your search.
    Sometimes a solution was already reported, and the problem is considered
    **solved**.

New issue reports should include information about your programming environment
(e.g., operating system, Python version) and steps to reproduce the problem.
Please try also to simplify the reproduction steps to a very minimal example
that still illustrates the problem you are facing. By removing other factors,
you help us to identify the root cause of the issue.

## Documentation improvements

You can help improve the documentation of `ape-utils` by making them more readable
and coherent, or by adding missing information and correcting mistakes.

This documentation uses [mkdocs] as its main documentation compiler.
This means that the docs are kept in the same repository as the project code, and
that any documentation update is done in the same way was a code contribution.

!!! tip
      Please notice that the [GitHub web interface] provides a quick way for
      proposing changes. While this mechanism can  be tricky for normal code contributions,
      it works perfectly fine for contributing to the docs, and can be quite handy.

      If you are interested in trying this method out, please navigate to
      the `docs` folder in the source [repository], find which file you
      would like to propose changes and click in the little pencil icon at the
      top, to open [GitHub's code editor]. Once you finish editing the file,
      please write a message in the form at the bottom of the page describing
      which changes have you made and what are the motivations behind them and
      submit your proposal.

When working on documentation changes in your local machine, you can
build and serve them using [hatch] with `hatch run docs:build` and
`hatch run docs:serve`, respectively.

## Code Contributions

### Submit an issue

Before you work on any non-trivial code contribution it's best to first create
a report in the [issue tracker] to start a discussion on the subject.
This often provides additional considerations and avoids unnecessary work.

### Clone the repository

1. Create a user account on GitHub if you do not already have one.

2. Fork the project [repository]: click on the *Fork* button near the top of the
   page. This creates a copy of the code under your account on GitHub.

3. Clone this copy to your local disk:

   ```console
   git clone git@github.com:YourLogin/ape-utils.git
   cd ape-utils
   ```

4. Make sure [hatch] is installed using [pipx]:

   ```console
   pipx install hatch
   ```

5. \[only once\] install [pre-commit] hooks in the default environment with:

   ```console
   hatch run pre-commit install
   ```

### Implement your changes

1. Create a branch to hold your changes:

   ```console
   git checkout -b my-feature
   ```

   and start making changes. Never work on the main branch!

2. Start your work on this branch. Don't forget to add [docstrings] in [Google style]
   to new functions, modules and classes, especially if they are part of public APIs.

3. Add yourself to the list of contributors in `AUTHORS.md`.

4. When you’re done editing, do:

   ```console
   git add <MODIFIED FILES>
   git commit
   ```

   to record your changes in [git].

   Please make sure to see the validation messages from [pre-commit] and fix
   any eventual issues.
   This should automatically use [flake8]/[black] to check/fix the code style
   in a way that is compatible with the project.

    !!! info
        Don't forget to add unit tests and documentation in case your
        contribution adds a feature and is not just a bugfix.

        Moreover, writing an [descriptive commit message] is highly recommended.
        In case of doubt, you can check the commit history with:
        ```
        git log --graph --decorate --pretty=oneline --abbrev-commit --all
        ```
        to look for recurring communication patterns.

5. Please check that your changes don't break any unit tests with
   `hatch run test:cov` or `hatch run test:no-cov` to run the unitest with
   or without coverage reports, respectively.

### Submit your contribution

1. If everything works fine, push your local branch to the remote server with:

   ```console
   git push -u origin my-feature
   ```

2. Go to the web page of your fork and click "Create pull request"
   to send your changes for review.

   Find more detailed information in [creating a PR]. You might also want to open
   the PR as a draft first and mark it as ready for review after the feedbacks
   from the continuous integration (CI) system or any required fixes.

Even though, these resources focus on open source projects and
communities, the general ideas behind collaborating with other developers
to collectively create software are general and can be applied to all sorts
of environments, including private companies and proprietary code bases.

## Pull Requests

Pull requests are welcomed! Please adhere to the following:

- Ensure your pull request passes our linting checks
- Include test cases for any new functionality
- Include any relevant documentation updates

It's a good idea to make pull requests early on.
A pull request represents the start of a discussion, and doesn't necessarily need to be the final, finished submission.

If you are opening a work-in-progress pull request to verify that it passes CI tests, please consider
[marking it as a draft](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests#draft-pull-requests).

Join the ApeWorX [Discord](https://discord.gg/apeworx) if you have any questions.

[black]: https://pypi.org/project/black/
[creating a PR]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request
[docstrings]: https://peps.python.org/pep-0257/
[flake8]: https://flake8.pycqa.org/en/stable/
[git]: https://git-scm.com
[github web interface]: https://docs.github.com/en/github/managing-files-in-a-repository/managing-files-on-github/editing-files-in-your-repository
[pre-commit]: https://pre-commit.com/
[pipx]: https://pypa.github.io/pipx/
[Google style]: https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings
