# TUTORIAL

This tutorial deals with the basics of GitHub and the Python programming language. The main audience consists of researchers, especially originating from STEM. Through many examples we will illustrate both general and particular functionnalities usefull when programming or carrying out scientific related work.

## 00 Introduction to GitHub

### Purpose

In this first section we will see what is GitHub, why we use it, and how.

Git is a distributed version control (DVC) system that allows to manage a program and its versions and track the changes made by programmers. This is very convenient as it allows to revert any change, maintain various versions of a program.

GitHub (or GitLab) is a more advanced implementation of Git providing additionnal functionnalities on top of Git such as hosting on a remote server, access control, sharing, feature requests, wiki or discussion. Github is designed to host, track and share computer programs in a collaborative environment. Each program is stored in a separate repository located on a remote server. To work on the program, a local user clones the repository in order to have a copy of the program locally. Then once the modification is satisfying it must be sent back to the remote server for everyone to enjoy it. Think about the remote version as the official one.

### Workflow

The main workflow is then as follows :
create or clone the repository > change the program > commit the changes > push the changes > change the program > and so on

Everything can be done either through command line interface (CLI) or graphical interface (GitHub desktop). I recommend using the Github desktop application.

If one wants to modify the program without risking breaking it, a parallel branch can be created. The main branch will be unaffected, ensuring the changes do not break a program that is being used. Then once the new branch is satisfying (it is checked for functionnalities and bugs), you can merge it with the main branch in order to implement its features in the main branch.
The possibility to create branches should not be used recklessly (wow !). It is not a way to maintain several sustainable versions of a program. You should do releases.

### Recommendations

One commit should cover one change and have an explicit comment. This makes tracking change and reverting them a confortable experience. If you change 20 things and do one commit with an oblivious name such as 'update' then good luck with correcting your mistakes afterwards.

Each GitHub repository should contain a documentation. A `README.md` explaining the purpose of the program and its main features is the minimum you can do. What you are reading is an example of `README.md`. Because it is written in markdown, you can structure it with titles, *format* **text**, insert [hyperlinks](https://www.youtube.com/watch?v=dQw4w9WgXcQ). More importantly you can write nice $\LaTeX$ equations ($U=RI$, $\frac{1}{2}mv^2$), which is very convenient to explain scientific code ! Do it.

There are few **<span style="color:red; font-size:18px">security</span>** concerns regarding the use of repositories. Every change is visible by the users of the repository and they can be reverted. If you store sensitive data in a repository, such as a private SSH key, confidential personnal information, passwords, etc. You will not be able to delete it entirely because of the tracking feature that allows to revert any changes. You will have to delete the entire repository, especially if it is public, as any random bot will sniff everything and scam you as soon as possible.

Do not store data on repositories. Indeed, because of this tracking functionnality, the repository will keep this heavy data in the history. So anyone working with the repository, will have to download it when cloning it locally. Repositories are not USB keys, it is a place to hold a program.

Also, GitHub is not a proper backup solution. You should always keep a backup somewhere.

### GitHub Copilot AI

As a scholar, Github provides an access to its GitHub copilot AI that can be implemented in an editor such as Visual Studio Code (VSC). VSC is a nice editor that I recommend. Do not overuse AI, AI is stupid.

## 10 Introduction to Python

In this section we will see what is Python, how to install and use it. The course will be the opportunity to get familiar with Python itself and practice the main features of Python. This is a nice introductory course to programming language in general.

Python is a free and open-source programming language widely used in a very broad range of fields such as web development, data science, artificial intelligence, scientific computing, graphical interface, command control, and much more ! Anything is possible with Python ! Due to its simplicity and readability, its huge active community, Python is ideal to learn programming in general.

## 20 Intermediary Python

In this section we will discuss Python functionnalities oriented towards scientific concerns.

## List of contributors
* Adrien Poindron
